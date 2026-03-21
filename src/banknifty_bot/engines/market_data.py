from abc import ABC, abstractmethod
from typing import List

from ..models import NewsSnapshot, OptionContract, OptionsChainSnapshot, SpotSnapshot


class MarketDataProvider(ABC):
    @abstractmethod
    def get_spot_snapshot(self) -> SpotSnapshot:
        raise NotImplementedError

    @abstractmethod
    def get_options_chain_snapshot(self) -> OptionsChainSnapshot:
        raise NotImplementedError


class NewsProvider(ABC):
    @abstractmethod
    def get_news_snapshot(self) -> NewsSnapshot:
        raise NotImplementedError


class DummyMarketDataProvider(MarketDataProvider):
    def get_spot_snapshot(self) -> SpotSnapshot:
        return SpotSnapshot(
            spot_price=48200.0,
            trend_score=18.0,
            trigger_score=26.0,
            signal_candle_high=48280.0,
            signal_candle_low=48140.0,
        )

    def get_options_chain_snapshot(self) -> OptionsChainSnapshot:
        ce = OptionContract(
            symbol='BANKNIFTY_DUMMY_CE',
            strike=48300.0,
            option_type='CE',
            expiry='weekly',
            ltp=112.5,
            volume=12000,
            open_interest=54000,
            distance_from_spot=100.0,
            liquidity_score=82.0,
            premium_score=74.0,
        )
        pe = OptionContract(
            symbol='BANKNIFTY_DUMMY_PE',
            strike=48100.0,
            option_type='PE',
            expiry='weekly',
            ltp=109.0,
            volume=11800,
            open_interest=51000,
            distance_from_spot=100.0,
            liquidity_score=79.0,
            premium_score=70.0,
        )
        return OptionsChainSnapshot(
            pcr=0.92,
            max_pain=48200.0,
            call_pressure_score=-24.0,
            put_pressure_score=12.0,
            selected_ce=ce,
            selected_pe=pe,
        )


class DummyNewsProvider(NewsProvider):
    def get_news_snapshot(self) -> NewsSnapshot:
        return NewsSnapshot(
            headline_count=5,
            sentiment_score=-8.0,
            risk_score=4.0,
            block_trade=False,
            reasons=['No high-risk macro event detected in dummy feed'],
        )
