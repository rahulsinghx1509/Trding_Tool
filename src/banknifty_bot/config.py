import os
from dataclasses import dataclass

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class Settings:
    app_env: str = os.getenv('APP_ENV', 'dev')
    dry_run: bool = os.getenv('DRY_RUN', 'true').lower() == 'true'
    bot_name: str = os.getenv('BOT_NAME', 'banknifty-alert-bot')
    scan_interval_seconds: int = int(os.getenv('SCAN_INTERVAL_SECONDS', '30'))

    capital: float = float(os.getenv('CAPITAL', '10000'))
    daily_max_loss_rupees: float = float(os.getenv('DAILY_MAX_LOSS_RUPEES', '500'))
    daily_max_loss_pct: float = float(os.getenv('DAILY_MAX_LOSS_PCT', '5'))
    max_reentries: int = int(os.getenv('MAX_REENTRIES', '1'))

    premium_stop_loss_pct: float = float(os.getenv('PREMIUM_STOP_LOSS_PCT', '25'))
    target_profit_pct: float = float(os.getenv('TARGET_PROFIT_PCT', '30'))
    trail_start_pct: float = float(os.getenv('TRAIL_START_PCT', '20'))
    trail_lock_pct: float = float(os.getenv('TRAIL_LOCK_PCT', '10'))
    time_exit: str = os.getenv('TIME_EXIT', '15:10')

    spot_weight: float = float(os.getenv('SPOT_WEIGHT', '40'))
    options_weight: float = float(os.getenv('OPTIONS_WEIGHT', '40'))
    news_weight: float = float(os.getenv('NEWS_WEIGHT', '20'))

    telegram_bot_token: str = os.getenv('TELEGRAM_BOT_TOKEN', '')
    telegram_chat_id: str = os.getenv('TELEGRAM_CHAT_ID', '')

    market_data_provider: str = os.getenv('MARKET_DATA_PROVIDER', 'angel_one')
    news_provider: str = os.getenv('NEWS_PROVIDER', 'news_api')


settings = Settings()
