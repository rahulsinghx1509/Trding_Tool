from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional


@dataclass
class SpotSnapshot:
    spot_price: float
    trend_score: float
    trigger_score: float
    signal_candle_high: Optional[float] = None
    signal_candle_low: Optional[float] = None
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class OptionContract:
    symbol: str
    strike: float
    option_type: str
    expiry: str
    ltp: float
    volume: int
    open_interest: int
    distance_from_spot: float
    liquidity_score: float
    premium_score: float


@dataclass
class OptionsChainSnapshot:
    pcr: float
    max_pain: Optional[float]
    call_pressure_score: float
    put_pressure_score: float
    selected_ce: Optional[OptionContract] = None
    selected_pe: Optional[OptionContract] = None
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class NewsSnapshot:
    headline_count: int
    sentiment_score: float
    risk_score: float
    block_trade: bool
    reasons: List[str]
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass
class ScoreBreakdown:
    spot_score: float
    options_score: float
    news_score: float
    weighted_total: float
    bias: str
    action: str
    reasons: List[str]


@dataclass
class PositionState:
    side: str
    symbol: str
    entry_price: float
    current_price: float
    signal_candle_level: float
    reentries_used: int = 0
    is_open: bool = True


@dataclass
class AlertCard:
    signal: str
    bias: str
    action: str
    symbol: str
    expiry: str
    strike: float
    premium: float
    stop_loss_text: str
    target_text: str
    trail_text: str
    reentry_text: str
    risk_note: str
    reasons: List[str]
    timestamp: datetime = field(default_factory=datetime.utcnow)
