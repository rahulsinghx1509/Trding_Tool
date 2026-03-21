from .config import settings
from .models import PositionState


def daily_loss_limit_reached(realized_pnl: float) -> bool:
    max_loss_by_pct = settings.capital * (settings.daily_max_loss_pct / 100.0)
    max_loss_allowed = min(settings.daily_max_loss_rupees, max_loss_by_pct)
    return realized_pnl <= (-1 * max_loss_allowed)


def premium_stop_loss_hit(entry_price: float, current_price: float) -> bool:
    stop_price = entry_price * (1 + settings.premium_stop_loss_pct / 100.0)
    return current_price >= stop_price


def premium_target_hit(entry_price: float, current_price: float) -> bool:
    target_price = entry_price * (1 - settings.target_profit_pct / 100.0)
    return current_price <= target_price


def trailing_lock_active(entry_price: float, current_price: float) -> bool:
    start_price = entry_price * (1 - settings.trail_start_pct / 100.0)
    return current_price <= start_price


def locked_profit_exit(entry_price: float, current_price: float) -> bool:
    locked_price = entry_price * (1 - settings.trail_lock_pct / 100.0)
    return current_price >= locked_price


def signal_candle_stop_hit(position: PositionState, spot_price: float) -> bool:
    if position.side == 'SELL_CE':
        return spot_price > position.signal_candle_level
    if position.side == 'SELL_PE':
        return spot_price < position.signal_candle_level
    return False
