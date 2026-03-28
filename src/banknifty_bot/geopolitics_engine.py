from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Sequence


@dataclass
class EventSignal:
    title: str
    source: str = 'manual'
    category: str = 'general'
    severity: float = 0.0
    direction: str = 'neutral'
    tags: List[str] | None = None


@dataclass
class GeoPoliticalAssessment:
    risk_score: float
    sentiment_score: float
    block_trade: bool
    market_bias: str
    reasons: List[str]
    detected_categories: List[str]


class GeoPoliticalEngine:
    """Rule-based geopolitical and macro analyzer.

    This module is intentionally provider-agnostic. It can consume headlines from any
    future source (news API, manual feed, broker notes, economic calendar, etc.) and
    convert them into a structured market-risk view for the bot.
    """

    CATEGORY_KEYWORDS = {
        'war': ['war', 'missile', 'airstrike', 'drone attack', 'border conflict', 'military escalation'],
        'oil': ['oil', 'crude', 'opec', 'supply cut', 'hormuz', 'energy shock'],
        'rates': ['fed', 'ecb', 'rbi', 'rate hike', 'rate cut', 'inflation', 'cpi', 'gdp'],
        'currency': ['dollar', 'usd', 'usdinr', 'devaluation', 'forex', 'currency'],
        'banking': ['bank collapse', 'liquidity crisis', 'default', 'credit event', 'downgrade'],
        'election': ['election', 'parliament', 'policy shock', 'tariff', 'sanction'],
        'weather': ['flood', 'cyclone', 'earthquake', 'wildfire', 'drought', 'monsoon'],
        'supply_chain': ['port closure', 'shipping disruption', 'container crisis', 'export ban'],
        'disease': ['pandemic', 'virus', 'outbreak', 'health emergency'],
        'india_specific': ['india', 'nse', 'bse', 'rbi', 'sebi', 'banknifty', 'nifty'],
    }

    CATEGORY_IMPACT = {
        'war': {'risk': 32.0, 'sentiment': -18.0},
        'oil': {'risk': 18.0, 'sentiment': -10.0},
        'rates': {'risk': 14.0, 'sentiment': -6.0},
        'currency': {'risk': 12.0, 'sentiment': -5.0},
        'banking': {'risk': 25.0, 'sentiment': -14.0},
        'election': {'risk': 10.0, 'sentiment': -4.0},
        'weather': {'risk': 8.0, 'sentiment': -3.0},
        'supply_chain': {'risk': 11.0, 'sentiment': -5.0},
        'disease': {'risk': 22.0, 'sentiment': -12.0},
        'india_specific': {'risk': 8.0, 'sentiment': -2.0},
    }

    POSITIVE_KEYWORDS = [
        'ceasefire', 'cooling inflation', 'rate cut', 'deal signed', 'supply restored',
        'liquidity support', 'stimulus', 'production increase', 'peace talks', 'disinflation',
    ]

    NEGATIVE_KEYWORDS = [
        'escalation', 'surge', 'attack', 'shock', 'sanction', 'cut', 'crisis', 'default',
        'sticky inflation', 'hawkish', 'uncertainty', 'emergency', 'disruption',
    ]

    def analyze(self, headlines: Sequence[str] | None = None, events: Iterable[EventSignal] | None = None) -> GeoPoliticalAssessment:
        reasons: List[str] = []
        categories: List[str] = []
        risk_score = 0.0
        sentiment_score = 0.0

        for headline in headlines or []:
            h = headline.lower().strip()
            matched = False
            for category, keywords in self.CATEGORY_KEYWORDS.items():
                if any(keyword in h for keyword in keywords):
                    matched = True
                    categories.append(category)
                    risk_score += self.CATEGORY_IMPACT[category]['risk']
                    sentiment_score += self.CATEGORY_IMPACT[category]['sentiment']
                    reasons.append(f'Headline matched {category}: {headline}')
            if any(word in h for word in self.POSITIVE_KEYWORDS):
                sentiment_score += 7.0
                risk_score -= 3.0
                reasons.append(f'Positive stabilizer detected: {headline}')
            if any(word in h for word in self.NEGATIVE_KEYWORDS):
                sentiment_score -= 6.0
                risk_score += 5.0
                reasons.append(f'Negative escalation language detected: {headline}')
            if not matched:
                reasons.append(f'Unclassified headline monitored: {headline}')

        for event in events or []:
            categories.append(event.category)
            risk_score += max(0.0, event.severity)
            if event.direction == 'risk_on':
                sentiment_score += max(0.0, event.severity * 0.4)
            elif event.direction == 'risk_off':
                sentiment_score -= max(0.0, event.severity * 0.5)
            reasons.append(f'Event signal added: {event.title} | {event.category} | {event.direction}')

        risk_score = max(0.0, min(100.0, risk_score))
        sentiment_score = max(-100.0, min(100.0, sentiment_score))

        if risk_score >= 55:
            block_trade = True
            market_bias = 'risk_off'
        elif sentiment_score <= -20:
            block_trade = False
            market_bias = 'bearish'
        elif sentiment_score >= 20:
            block_trade = False
            market_bias = 'bullish'
        else:
            block_trade = False
            market_bias = 'neutral'

        return GeoPoliticalAssessment(
            risk_score=round(risk_score, 2),
            sentiment_score=round(sentiment_score, 2),
            block_trade=block_trade,
            market_bias=market_bias,
            reasons=reasons,
            detected_categories=sorted(set(categories)),
        )


def build_event_signals(raw_events: Sequence[dict]) -> List[EventSignal]:
    signals: List[EventSignal] = []
    for row in raw_events:
        signals.append(
            EventSignal(
                title=str(row.get('title', '')),
                source=str(row.get('source', 'manual')),
                category=str(row.get('category', 'general')),
                severity=float(row.get('severity', 0.0) or 0.0),
                direction=str(row.get('direction', 'neutral')),
                tags=list(row.get('tags', []) or []),
            )
        )
    return signals
