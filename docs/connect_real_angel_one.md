# Connect Real Angel One Account

## Important

Do not paste secrets in chat.
Keep them only in your local `.env` file.

## 1. Install required packages

Use your local terminal inside the project:

```bash
pip install -r requirements.txt
pip install pyotp
```

Also install the official SmartAPI Python SDK in the environment where you will run the bot.

## 2. Create local `.env`

Copy `.env.example` to `.env` and fill these values:

```env
APP_ENV=dev
DRY_RUN=true

BOT_NAME=banknifty-alert-bot
SCAN_INTERVAL_SECONDS=30

CAPITAL=10000
DAILY_MAX_LOSS_RUPEES=500
DAILY_MAX_LOSS_PCT=5
MAX_REENTRIES=1

PREMIUM_STOP_LOSS_PCT=25
TARGET_PROFIT_PCT=30
TRAIL_START_PCT=20
TRAIL_LOCK_PCT=10
TIME_EXIT=15:10

SPOT_WEIGHT=40
OPTIONS_WEIGHT=40
NEWS_WEIGHT=20

MARKET_DATA_PROVIDER=angel_one
NEWS_PROVIDER=dummy
ANGEL_BASE_URL=https://apiconnect.angelone.in

ANGEL_CLIENT_ID=your_client_code
ANGEL_API_KEY=your_api_key
ANGEL_PIN=your_pin
ANGEL_TOTP_SECRET=your_totp_secret

TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
```

## 3. Start in dry-run only

Do not begin with live execution.
First confirm only these work:
- SmartAPI login
- BankNifty spot fetch
- candle fetch
- Telegram send

## 4. Current repo reality

The repo has the SmartAPI adapter scaffold and bot framework, but it still needs final runtime wiring for:
- live SmartAPI auth path
- live BankNifty spot/candle mapping into `SpotSnapshot`
- richer live option-chain mapping

So filling `.env` alone is not the final step.

## 5. Safe test order

1. Confirm SmartAPI credentials work in isolation
2. Confirm TOTP generation works
3. Confirm one BankNifty LTP request works
4. Confirm one candle request works
5. Confirm Telegram test alert works
6. Then plug those into the bot runtime

## 6. What not to do

- do not hardcode secrets in source files
- do not commit `.env`
- do not start with auto-trading
- do not test first on live order placement
