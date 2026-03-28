# Geopolitical Engine

## Purpose

This module adds a separate geopolitical and macro-risk layer to the bot.

It is designed to evaluate:
- wars and border escalations
- crude/oil shocks
- central bank and inflation events
- currency stress
- banking crises and defaults
- elections, sanctions, tariff shocks
- weather and supply-chain disruptions
- disease/pandemic-type events
- India-specific macro and market events

## File

- `src/banknifty_bot/geopolitics_engine.py`

## Output

The engine returns:
- `risk_score`
- `sentiment_score`
- `block_trade`
- `market_bias`
- `reasons`
- `detected_categories`

## How it should be used

This engine should feed into the broader news/risk layer.

Suggested integration path:

1. fetch headlines/events from any source
2. pass them into `GeoPoliticalEngine.analyze(...)`
3. map the output into the bot's news snapshot
4. let the signal engine use that result as part of the 20% news weight

## Important limitation

This is currently rule-based, not an LLM/news-search system.

That is deliberate:
- deterministic
- easy to audit
- no dependency on external AI calls
- safer for first-stage trading infra

## Next improvement

Later we can extend it with:
- economic calendar ingestion
- structured RBI/FED event calendar
- commodity move filters
- USDINR / VIX / crude impact model
- source-weighted headline scoring
