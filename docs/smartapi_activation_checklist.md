# Angel One SmartAPI Activation Checklist

## Current status

SmartAPI access is **not active yet**.

That means:
- live broker authentication cannot be completed yet
- live market data fetch cannot be tested yet
- live BankNifty signal flow cannot be verified against broker data yet
- live order placement must remain disabled

## What you need to activate

1. Angel One trading account must be active
2. SmartAPI access must be enabled on your account
3. API key / app setup must be created in Angel One developer portal
4. You should have access to:
   - client code
   - API key
   - PIN/password as required by your broker login flow
   - TOTP setup for login
5. Network/IP/device restrictions, if any, should be checked in your account settings

## What we can still build right now

Even without live SmartAPI activation, this repo can continue moving forward in a clean way:

1. finish broker interface structure
2. add instrument master loader
3. add BankNifty strike/expiry resolver
4. add real signal engine logic over a mock feed
5. add Telegram message templates and command support
6. add paper-trade journal and CSV logs
7. add dry-run scheduler loop
8. add backtest/replay framework for strategy validation

## Recommended immediate path

Do this in order:

1. Activate SmartAPI
2. Keep the bot in dry-run mode first
3. Test live data only
4. Test Telegram alerts only
5. Validate signal quality
6. Only later consider paper trade / live execution

## Safe credential handling

Do not hardcode secrets in code.
Use `.env` for:
- `ANGEL_CLIENT_ID`
- `ANGEL_API_KEY`
- `ANGEL_TOTP_SECRET`
- `ANGEL_PIN`
- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`

## Suggested next coding step

Because SmartAPI is not active yet, the best next code step is:

**Build the BankNifty signal engine and paper/dry-run workflow independent of the broker.**

That keeps progress real and avoids blocking on account activation.
