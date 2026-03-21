from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Optional

from ..models import OptionContract, OptionsChainSnapshot


@dataclass
class ExpiryChoice:
    expiry: str
    score: float
    reason: str


@dataclass
class ResolvedContract:
    action: str
    chosen_expiry: str
    chosen_contract: OptionContract
    considered_expiries: List[ExpiryChoice]


class BankNiftyResolver:
    def __init__(
        self,
        strike_step: int = 100,
        weekly_bias_bonus: float = 3.0,
        monthly_stability_bonus: float = 2.0,
    ) -> None:
        self.strike_step = strike_step
        self.weekly_bias_bonus = weekly_bias_bonus
        self.monthly_stability_bonus = monthly_stability_bonus

    def nearest_strike(self, spot_price: float) -> int:
        return int(round(spot_price / self.strike_step) * self.strike_step)

    def score_expiry_candidates(self, contracts: Iterable[OptionContract]) -> List[ExpiryChoice]:
        grouped = {}
        for contract in contracts:
            expiry_key = contract.expiry.lower().strip()
            grouped.setdefault(expiry_key, []).append(contract)

        choices: List[ExpiryChoice] = []
        for expiry, items in grouped.items():
            avg_liquidity = sum(i.liquidity_score for i in items) / len(items)
            avg_premium = sum(i.premium_score for i in items) / len(items)
            avg_distance_penalty = sum(abs(i.distance_from_spot) for i in items) / len(items)

            score = (avg_liquidity * 0.45) + (avg_premium * 0.45) - (avg_distance_penalty * 0.02)
            reason = 'balanced liquidity and premium behavior'

            if 'weekly' in expiry:
                score += self.weekly_bias_bonus
                reason = 'weekly preferred due to closer expiry and tradability'
            elif 'monthly' in expiry:
                score += self.monthly_stability_bonus
                reason = 'monthly preferred due to stability and lower expiry noise'

            choices.append(ExpiryChoice(expiry=expiry, score=round(score, 2), reason=reason))

        return sorted(choices, key=lambda x: x.score, reverse=True)

    def resolve(self, action: str, chain: OptionsChainSnapshot, spot_price: float) -> Optional[ResolvedContract]:
        candidates = []
        if chain.selected_ce is not None:
            candidates.append(chain.selected_ce)
        if chain.selected_pe is not None:
            candidates.append(chain.selected_pe)

        if not candidates:
            return None

        expiry_choices = self.score_expiry_candidates(candidates)
        if not expiry_choices:
            return None

        best_expiry = expiry_choices[0].expiry
        filtered = [c for c in candidates if c.expiry.lower().strip() == best_expiry]

        if action == 'SELL_CE_ALERT':
            filtered = [c for c in filtered if c.option_type.upper() == 'CE']
        elif action == 'SELL_PE_ALERT':
            filtered = [c for c in filtered if c.option_type.upper() == 'PE']

        if not filtered:
            return None

        target_strike = self.nearest_strike(spot_price)
        chosen = min(
            filtered,
            key=lambda c: (
                abs(c.strike - target_strike),
                -1 * c.liquidity_score,
                -1 * c.premium_score,
            ),
        )

        return ResolvedContract(
            action=action,
            chosen_expiry=best_expiry,
            chosen_contract=chosen,
            considered_expiries=expiry_choices,
        )
