from __future__ import annotations

import csv
from pathlib import Path
from typing import Optional

from .signal_engine import SignalDecision


class PaperJournal:
    def __init__(self, filepath: str = 'data/paper_journal.csv') -> None:
        self.path = Path(filepath)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._ensure_header()

    def _ensure_header(self) -> None:
        if self.path.exists():
            return
        with self.path.open('w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                'timestamp',
                'action',
                'bias',
                'blocked',
                'weighted_total',
                'spot_score',
                'options_score',
                'news_score',
                'symbol',
                'strike',
                'expiry',
                'premium',
                'reasons',
            ])

    def record(self, decision: SignalDecision) -> None:
        contract = decision.selected_contract
        with self.path.open('a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                getattr(decision.score_breakdown, 'weighted_total', ''),
                decision.action,
                decision.bias,
                decision.blocked,
                decision.score_breakdown.weighted_total,
                decision.score_breakdown.spot_score,
                decision.score_breakdown.options_score,
                decision.score_breakdown.news_score,
                getattr(contract, 'symbol', ''),
                getattr(contract, 'strike', ''),
                getattr(contract, 'expiry', ''),
                getattr(contract, 'ltp', ''),
                ' | '.join(decision.reasons),
            ])
