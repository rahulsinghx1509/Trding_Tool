from dataclasses import dataclass
from typing import Any, Dict, Optional

import requests

from ..models import NewsSnapshot, OptionsChainSnapshot, SpotSnapshot


@dataclass
class AngelOneCredentials:
    api_key: str
    client_id: str
    pin: str
    totp_secret: str


class AngelOneClient:
    """Lightweight Angel One client scaffold.

    This is intentionally conservative. It provides the shape required for
    authentication and market-data access, but leaves broker-specific request
    details to be filled after credentials and endpoint choices are confirmed.
    """

    def __init__(self, credentials: AngelOneCredentials, base_url: str, timeout: int = 15) -> None:
        self.credentials = credentials
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()
        self.auth_token: Optional[str] = None
        self.refresh_token: Optional[str] = None
        self.feed_token: Optional[str] = None

    def set_access_tokens(
        self,
        auth_token: Optional[str] = None,
        refresh_token: Optional[str] = None,
        feed_token: Optional[str] = None,
    ) -> None:
        self.auth_token = auth_token
        self.refresh_token = refresh_token
        self.feed_token = feed_token

    def default_headers(self) -> Dict[str, str]:
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-PrivateKey': self.credentials.api_key,
        }
        if self.auth_token:
            headers['Authorization'] = f'Bearer {self.auth_token}'
        return headers

    def authenticate(self) -> Dict[str, Any]:
        """Placeholder auth method.

        Real request payload and TOTP generation should be added after we lock the
        exact Angel One auth flow you want to use in code.
        """
        raise NotImplementedError('Angel One authentication flow has not been wired yet.')

    def get_ltp(self, exchange: str, tradingsymbol: str, symboltoken: str) -> Dict[str, Any]:
        raise NotImplementedError('Angel One LTP endpoint wiring pending.')

    def get_candles(self, params: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError('Angel One candle endpoint wiring pending.')

    def get_option_chain(self, params: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError('Option-chain source wiring pending.')


class AngelOneMarketDataProvider:
    """Provider that will replace the dummy provider once live broker wiring is done."""

    def __init__(self, client: AngelOneClient) -> None:
        self.client = client

    def get_spot_snapshot(self) -> SpotSnapshot:
        raise NotImplementedError('Spot snapshot mapping from Angel One market data is pending.')

    def get_options_chain_snapshot(self) -> OptionsChainSnapshot:
        raise NotImplementedError('Options chain snapshot mapping is pending.')


class PlaceholderNewsProvider:
    def get_news_snapshot(self) -> NewsSnapshot:
        return NewsSnapshot(
            headline_count=0,
            sentiment_score=0.0,
            risk_score=0.0,
            block_trade=False,
            reasons=['Live news provider not configured yet'],
        )
