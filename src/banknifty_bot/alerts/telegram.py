import requests

from ..config import settings
from ..models import AlertCard


class TelegramAlertSender:
    def __init__(self) -> None:
        self.bot_token = settings.telegram_bot_token
        self.chat_id = settings.telegram_chat_id

    def is_configured(self) -> bool:
        return bool(self.bot_token and self.chat_id)

    def format_alert(self, alert: AlertCard) -> str:
        reasons = '\n'.join([f'- {r}' for r in alert.reasons])
        return (
            f'📣 {alert.signal}\n'
            f'Bias: {alert.bias}\n'
            f'Action: {alert.action}\n'
            f'Symbol: {alert.symbol}\n'
            f'Expiry: {alert.expiry}\n'
            f'Strike: {alert.strike}\n'
            f'Premium: {alert.premium}\n'
            f'SL: {alert.stop_loss_text}\n'
            f'Target: {alert.target_text}\n'
            f'Trail: {alert.trail_text}\n'
            f'Re-entry: {alert.reentry_text}\n'
            f'Risk: {alert.risk_note}\n'
            f'Reasons:\n{reasons}'
        )

    def send(self, alert: AlertCard) -> None:
        message = self.format_alert(alert)
        if not self.is_configured():
            print('\n[Telegram not configured]')
            print(message)
            return

        url = f'https://api.telegram.org/bot{self.bot_token}/sendMessage'
        payload = {
            'chat_id': self.chat_id,
            'text': message,
        }
        response = requests.post(url, json=payload, timeout=15)
        response.raise_for_status()
