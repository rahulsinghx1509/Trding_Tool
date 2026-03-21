import argparse

from .alerts.telegram import TelegramAlertSender
from .config import settings
from .engines.market_data import DummyMarketDataProvider, DummyNewsProvider
from .scoring import compute_weighted_score
from .selectors.contract_selector import choose_contract
from .utils import build_alert_card


def run_once() -> None:
    market_provider = DummyMarketDataProvider()
    news_provider = DummyNewsProvider()
    alert_sender = TelegramAlertSender()

    spot = market_provider.get_spot_snapshot()
    chain = market_provider.get_options_chain_snapshot()
    news = news_provider.get_news_snapshot()

    score = compute_weighted_score(spot=spot, options_chain=chain, news=news)
    contract = choose_contract(score.action, chain)

    if contract is None:
        print(f'Action: {score.action} | Bias: {score.bias}')
        print('Reasons:')
        for reason in score.reasons:
            print(f'- {reason}')
        return

    alert = build_alert_card(score=score, contract=contract, max_reentries=settings.max_reentries)
    alert_sender.send(alert)


def main() -> None:
    parser = argparse.ArgumentParser(description='BankNifty alert bot runner')
    parser.add_argument('--dry-run', action='store_true', help='Run one dry cycle')
    args = parser.parse_args()

    if args.dry_run or settings.dry_run:
        run_once()
        return

    run_once()
