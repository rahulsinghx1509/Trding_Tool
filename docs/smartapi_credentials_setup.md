# SmartAPI Credential Setup

## Do not paste secrets in chat

Keep all broker credentials in your local `.env` file.

## Required values

Fill these in `.env`:

- `ANGEL_CLIENT_ID`
- `ANGEL_API_KEY`
- `ANGEL_PIN`
- `ANGEL_TOTP_SECRET`
- `ANGEL_BASE_URL`
- `MARKET_DATA_PROVIDER=angel_one`

## Telegram values

Also fill:

- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`

## Expected next use

Once credentials are filled, the bot should be able to:

1. create broker session
2. fetch BankNifty spot data
3. fetch candles
4. later fetch richer option-chain data
5. send Telegram alerts from real market data

## Safety

- never commit `.env`
- never hardcode tokens in code
- start with dry-run mode only
