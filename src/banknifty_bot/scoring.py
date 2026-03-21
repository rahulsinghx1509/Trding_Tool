from banknifty_bot.config import settings
from banknifty_bot.models import NewsSnapshot, OptionsChainSnapshot, ScoreBreakdown, SpotSnapshot


def clamp_score(value: float, low: float = -100.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def compute_weighted_score(
    spot: SpotSnapshot,
    options_chain: OptionsChainSnapshot,
    news: NewsSnapshot,
) -> ScoreBreakdown:
    spot_score = clamp_score((spot.trend_score * 0.6) + (spot.trigger_score * 0.4))

    if options_chain.call_pressure_score > options_chain.put_pressure_score:
        options_score = clamp_score(options_chain.call_pressure_score)
    else:
        options_score = clamp_score(-1 * options_chain.put_pressure_score)

    news_score = clamp_score(news.sentiment_score - news.risk_score)

    total_weight = settings.spot_weight + settings.options_weight + settings.news_weight
    weighted_total = (
        (spot_score * settings.spot_weight)
        + (options_score * settings.options_weight)
        + (news_score * settings.news_weight)
    ) / total_weight

    reasons = []
    if news.block_trade:
        reasons.append('News engine marked high-risk event day')

    if weighted_total <= -20:
        bias = 'bearish'
        action = 'SELL_CE_ALERT'
        reasons.append('Weighted score supports bearish premium-selling bias')
    elif weighted_total >= 20:
        bias = 'bullish'
        action = 'SELL_PE_ALERT'
        reasons.append('Weighted score supports bullish premium-selling bias')
    else:
        bias = 'neutral'
        action = 'NO_TRADE'
        reasons.append('No edge strong enough after score merge')

    if news.block_trade:
        action = 'NO_TRADE'
        bias = 'risk_off'

    return ScoreBreakdown(
        spot_score=round(spot_score, 2),
        options_score=round(options_score, 2),
        news_score=round(news_score, 2),
        weighted_total=round(weighted_total, 2),
        bias=bias,
        action=action,
        reasons=reasons + news.reasons,
    )
