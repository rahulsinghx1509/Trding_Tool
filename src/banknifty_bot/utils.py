from datetime import datetime

from .models import AlertCard, OptionContract, ScoreBreakdown


def build_alert_card(
    score: ScoreBreakdown,
    contract: OptionContract,
    max_reentries: int,
) -> AlertCard:
    signal = 'ENTRY ALERT' if 'SELL' in score.action else 'NO TRADE'
    return AlertCard(
        signal=signal,
        bias=score.bias,
        action=score.action,
        symbol=contract.symbol,
        expiry=contract.expiry,
        strike=contract.strike,
        premium=contract.ltp,
        stop_loss_text='25% premium SL + signal candle invalidation',
        target_text='30% premium decay target',
        trail_text='Trail starts at 20%, lock 10%',
        reentry_text=f'Max re-entries allowed: {max_reentries}',
        risk_note='Daily stop at INR 500 or 5% of capital, whichever hits first',
        reasons=score.reasons,
        timestamp=datetime.utcnow(),
    )
