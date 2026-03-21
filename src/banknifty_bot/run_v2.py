from __future__ import annotations

from .alerts.telegram import TelegramAlertSender
from .journal import PaperJournal
from .signal_engine import SignalEngine
from .selectors.resolver import BankNiftyResolver
from .utils import build_alert_card
from .engines.mock_market_v2 import RichMockMarketProvider, RichMockNewsProvider


def run_v2_dry() -> None:
    market_provider = RichMockMarketProvider()
    news_provider = RichMockNewsProvider()
    signal_engine = SignalEngine()
    resolver = BankNiftyResolver()
    journal = PaperJournal(filepath='data/paper_journal_v2.csv')
    alert_sender = TelegramAlertSender()

    spot = market_provider.get_spot_snapshot()
    chain = market_provider.get_options_chain_snapshot()
    news = news_provider.get_news_snapshot()

    decision = signal_engine.evaluate(
        spot=spot,
        options_chain=chain,
        news=news,
        realized_pnl=0.0,
        reentries_used=0,
        max_reentries=1,
    )

    if decision.selected_contract is None:
        journal.record(decision)
        print(f'Action: {decision.action} | Bias: {decision.bias}')
        for reason in decision.reasons:
            print(f'- {reason}')
        return

    resolved = resolver.resolve(
        action=decision.action,
        chain=chain,
        spot_price=spot.spot_price,
    )

    if resolved is None:
        journal.record(decision)
        print('Resolver failed to choose a contract')
        return

    decision.selected_contract = resolved.chosen_contract
    journal.record(decision)

    alert = build_alert_card(
        score=decision.score_breakdown,
        contract=resolved.chosen_contract,
        max_reentries=1,
    )
    alert_sender.send(alert)


if __name__ == '__main__':
    run_v2_dry()
