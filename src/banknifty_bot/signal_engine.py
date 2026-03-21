from dataclasses import dataclass
from typing import List, Optional

from .models import NewsSnapshot, OptionContract, OptionsChainSnapshot, ScoreBreakdown, SpotSnapshot
from .risk import daily_loss_limit_reached
from .scoring import compute_weighted_score


@dataclass
class SignalDecision:
    action: str
    bias: str
    score_breakdown: ScoreBreakdown
    selected_contract: Optional[OptionContract]
    blocked: bool
    reasons: List[str]


class SignalEngine:
    def __init__(
        self,
        entry_threshold: float = 20.0,
        strong_threshold: float = 35.0,
        neutral_band: float = 12.0,
        max_spread_pct: float = 12.0,
    ) -> None:
        self.entry_threshold = entry_threshold
        self.strong_threshold = strong_threshold
        self.neutral_band = neutral_band
        self.max_spread_pct = max_spread_pct

    def evaluate(
        self,
        spot: SpotSnapshot,
        options_chain: OptionsChainSnapshot,
        news: NewsSnapshot,
        realized_pnl: float = 0.0,
        reentries_used: int = 0,
        max_reentries: int = 1,
    ) -> SignalDecision:
        score = compute_weighted_score(spot=spot, options_chain=options_chain, news=news)
        reasons = list(score.reasons)
        blocked = False
        selected_contract: Optional[OptionContract] = None

        if daily_loss_limit_reached(realized_pnl):
            blocked = True
            reasons.append('Daily max loss reached')

        if reentries_used > max_reentries:
            blocked = True
            reasons.append('Re-entry cap reached')

        if news.block_trade:
            blocked = True
            reasons.append('News filter blocked trading')

        weighted_total = score.weighted_total
        if abs(weighted_total) < self.neutral_band:
            blocked = True
            reasons.append('Score in no-trade neutral band')

        if score.action == 'SELL_CE_ALERT':
            selected_contract = options_chain.selected_ce
        elif score.action == 'SELL_PE_ALERT':
            selected_contract = options_chain.selected_pe

        if selected_contract is None:
            blocked = True
            reasons.append('No valid option contract selected')

        if selected_contract is not None and not self._contract_is_tradeable(selected_contract):
            blocked = True
            reasons.append('Selected contract failed liquidity/premium sanity checks')

        if blocked:
            return SignalDecision(
                action='NO_TRADE',
                bias='risk_off' if news.block_trade else score.bias,
                score_breakdown=score,
                selected_contract=None,
                blocked=True,
                reasons=reasons,
            )

        if abs(weighted_total) >= self.strong_threshold:
            reasons.append('Strong conviction setup detected')
        elif abs(weighted_total) >= self.entry_threshold:
            reasons.append('Base entry threshold passed')
        else:
            return SignalDecision(
                action='NO_TRADE',
                bias='neutral',
                score_breakdown=score,
                selected_contract=None,
                blocked=True,
                reasons=reasons + ['Threshold not strong enough for trade'],
            )

        return SignalDecision(
            action=score.action,
            bias=score.bias,
            score_breakdown=score,
            selected_contract=selected_contract,
            blocked=False,
            reasons=reasons,
        )

    def _contract_is_tradeable(self, contract: OptionContract) -> bool:
        if contract.ltp <= 0:
            return False
        if contract.volume <= 0 or contract.open_interest <= 0:
            return False
        if contract.liquidity_score < 50:
            return False
        if contract.premium_score < 45:
            return False
        return True
