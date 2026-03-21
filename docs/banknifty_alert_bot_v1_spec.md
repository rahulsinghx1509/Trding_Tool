# BankNifty Alert Bot v1 Specification

## Locked scope

- Broker: Angel One
- Instrument: BankNifty Options
- Mode: Alert-only
- Strategy family: Selling-first
- Directions: CE sell and PE sell both
- Inputs: Spot + options chain + news filter
- News behavior:
  - shift bias (bullish / bearish / neutral / no-trade)
  - block trades on high-risk event conditions
- Alert delivery: Telegram
- Alert format: Full alert card
- Scan frequency: Every 30 seconds
- Capital reference: INR 10,000
- Re-entry cap: 1
- Premium stop loss: 25%
- Spot stop loss: Signal candle invalidation level
- Fixed target: 30%
- Trail start: 20%
- Profit lock: 10%
- Time exit: 3:10 PM
- Expiry selection: Smart choice using liquidity + premium behavior + distance to expiry
- Timeframe logic: Multi-timeframe
  - 5-minute for structure/trend
  - 1-minute for trigger
  - 30-second scan for evaluation frequency
- Decision engine weights:
  - Spot: 40
  - Options chain: 40
  - News: 20
- Daily mode: Multiple trades per day with one re-entry only

## High-level architecture

1. Market data engine
   - BankNifty spot/index data
   - options chain data
   - candles for 1-minute and 5-minute views

2. News and risk engine
   - headline ingestion
   - event-risk detection
   - sentiment / risk score
   - trade block logic on high-risk days

3. Decision engine
   - compute spot score
   - compute options-chain score
   - compute news/risk score
   - combine weighted score into final action:
     - SELL_CE_ALERT
     - SELL_PE_ALERT
     - EXIT_ALERT
     - NO_TRADE

4. Risk engine
   - premium-based SL
   - spot invalidation SL
   - re-entry cap
   - daily max loss guard (final threshold pending)
   - time-based forced exit
   - target and trailing-profit logic

5. Alert engine
   - Telegram delivery
   - full alert card with:
     - signal
     - bias
     - reason summary
     - expiry choice
     - strike suggestion
     - premium / entry zone
     - stop loss
     - target
     - trail state
     - re-entry state
     - risk note

## Open items still to lock

- exact daily max loss rule
- exact score thresholds for SELL_CE / SELL_PE / NO_TRADE / EXIT
- signal candle definition
- strike selection method
- news source/API
- market data source/API details from Angel One
- Telegram bot wiring details
- run environment (local / VPS)

## v1 delivery plan

- Step 1: finalize remaining trading rules
- Step 2: create project structure and configuration files
- Step 3: implement market, news, scoring, risk, and alert modules
- Step 4: implement dry-run loop and sample Telegram alerts
- Step 5: add Angel One integration points
- Step 6: backtest/simulation hooks for later validation
