# BankNifty Resolver Notes

## Purpose

The resolver layer chooses the best option contract for a signal after the signal engine has decided the action.

It currently does 3 things:

1. score expiry buckets
2. estimate nearest tradable strike from spot
3. choose the best CE/PE contract by action, expiry, distance, liquidity, and premium quality

## Current logic

### Expiry scoring

Each expiry bucket is scored on:
- liquidity score
- premium score
- distance from spot penalty

Bias bonuses:
- weekly expiry gets a small tradability bonus
- monthly expiry gets a small stability bonus

### Strike resolution

Nearest strike is rounded using a configurable `strike_step`.
Default is `100`, aligned with BankNifty option strike increments.

### Final selection order

The chosen contract is based on:
1. action match (CE or PE)
2. best expiry score
3. nearest strike to rounded spot
4. higher liquidity score
5. higher premium score

## Current limitation

Right now the dummy market provider exposes only one CE and one PE candidate. So the resolver logic is structurally correct, but not fully exercised yet.

## Next improvement

To make the resolver real, the next step should be:
- feed a richer mock option chain with multiple strikes and both weekly/monthly contracts
- later replace that with live instrument master + market data
