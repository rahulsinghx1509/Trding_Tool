# Trding_Tool

BankNifty alert-only trading bot skeleton for Angel One.

## What this version does

This is the first codebase scaffold for your v1 bot. It is built around the locked spec in `docs/banknifty_alert_bot_v1_spec.md`.

Current scope:
- BankNifty only
- alert-only mode
- selling-first logic
- CE and PE sell alerts
- weighted decision engine using spot + options chain + news filter
- Telegram alert plumbing
- risk engine with stop, target, trail, and daily loss controls
- dry-run loop for local development

## Project layout

```text
.
├── docs/
├── src/
│   └── banknifty_bot/
│       ├── alerts/
│       ├── engines/
│       ├── selectors/
│       ├── config.py
│       ├── models.py
│       ├── scoring.py
│       ├── risk.py
│       └── runner.py
├── .env.example
├── main.py
└── requirements.txt
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python main.py --dry-run
```

## Environment variables

Keep secrets in `.env`, never in code.

Important fields:
- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`
- `ANGEL_CLIENT_ID`
- `ANGEL_API_KEY`
- `ANGEL_TOTP_SECRET`
- `NEWS_API_KEY`

## Notes

- This version does **not** place live trades.
- It is designed to be extended with Angel One live market data and a real news provider.
- Telegram sending is implemented as a clean interface and can be tested once you fill `.env`.

## Next implementation step

After this scaffold, we should wire:
1. Angel One market data
2. options chain source
3. news provider
4. live scoring thresholds
5. Telegram credentials
