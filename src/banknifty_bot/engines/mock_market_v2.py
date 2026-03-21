from __future__ import annotations

from typing import List

from ..models import NewsSnapshot, OptionContract, OptionsChainSnapshot, SpotSnapshot


class RichMockMarketProvider:
    def get_spot_snapshot(self) -> SpotSnapshot:
        return SpotSnapshot(
            spot_price=48235.0,
            trend_score=22.0,
            trigger_score=28.0,
            signal_candle_high=48305.0,
            signal_candle_low=48190.0,
        )

    def get_option_contracts(self) -> List[OptionContract]:
        return [
            OptionContract('BANKNIFTY_WEEKLY_48100_CE', 48100.0, 'CE', 'weekly', 158.0, 14000, 81000, 135.0, 84.0, 76.0),
            OptionContract('BANKNIFTY_WEEKLY_48200_CE', 48200.0, 'CE', 'weekly', 121.0, 15500, 86000, 35.0, 88.0, 79.0),
            OptionContract('BANKNIFTY_WEEKLY_48300_CE', 48300.0, 'CE', 'weekly', 96.0, 14900, 79000, 65.0, 86.0, 78.0),
            OptionContract('BANKNIFTY_MONTHLY_48100_CE', 48100.0, 'CE', 'monthly', 182.0, 9000, 52000, 135.0, 72.0, 70.0),
            OptionContract('BANKNIFTY_MONTHLY_48200_CE', 48200.0, 'CE', 'monthly', 144.0, 10200, 56000, 35.0, 75.0, 73.0),
            OptionContract('BANKNIFTY_MONTHLY_48300_CE', 48300.0, 'CE', 'monthly', 118.0, 9800, 54000, 65.0, 74.0, 72.0),
            OptionContract('BANKNIFTY_WEEKLY_48100_PE', 48100.0, 'PE', 'weekly', 88.0, 13000, 72000, 135.0, 82.0, 75.0),
            OptionContract('BANKNIFTY_WEEKLY_48200_PE', 48200.0, 'PE', 'weekly', 110.0, 14200, 81000, 35.0, 85.0, 77.0),
            OptionContract('BANKNIFTY_WEEKLY_48300_PE', 48300.0, 'PE', 'weekly', 141.0, 13600, 76000, 65.0, 83.0, 74.0),
            OptionContract('BANKNIFTY_MONTHLY_48100_PE', 48100.0, 'PE', 'monthly', 108.0, 8700, 47000, 135.0, 70.0, 69.0),
            OptionContract('BANKNIFTY_MONTHLY_48200_PE', 48200.0, 'PE', 'monthly', 132.0, 9300, 51000, 35.0, 73.0, 71.0),
            OptionContract('BANKNIFTY_MONTHLY_48300_PE', 48300.0, 'PE', 'monthly', 166.0, 9100, 49500, 65.0, 72.0, 70.0),
        ]

    def get_options_chain_snapshot(self) -> OptionsChainSnapshot:
        contracts = self.get_option_contracts()
        ce_candidates = [c for c in contracts if c.option_type == 'CE' and c.expiry == 'weekly']
        pe_candidates = [c for c in contracts if c.option_type == 'PE' and c.expiry == 'weekly']
        selected_ce = min(ce_candidates, key=lambda c: abs(c.distance_from_spot))
        selected_pe = min(pe_candidates, key=lambda c: abs(c.distance_from_spot))
        return OptionsChainSnapshot(
            pcr=0.97,
            max_pain=48200.0,
            call_pressure_score=-26.0,
            put_pressure_score=14.0,
            selected_ce=selected_ce,
            selected_pe=selected_pe,
        )


class RichMockNewsProvider:
    def get_news_snapshot(self) -> NewsSnapshot:
        return NewsSnapshot(
            headline_count=7,
            sentiment_score=-6.0,
            risk_score=3.0,
            block_trade=False,
            reasons=['Mock news feed indicates manageable macro risk'],
        )
