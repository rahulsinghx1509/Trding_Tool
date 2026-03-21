from dataclasses import dataclass
from typing import Dict, Optional

import requests


@dataclass
class SmartApiSession:
    jwt_token: Optional[str] = None
    refresh_token: Optional[str] = None
    feed_token: Optional[str] = None


class SmartApiAuthenticator:
    """Official-flow style authenticator scaffold for Angel One SmartAPI.

    This file intentionally separates auth concerns from strategy logic.
    The payload keys and exact endpoints should be confirmed before live use.
    """

    def __init__(self, api_key: str, client_code: str, password: str, totp_code: str, base_url: str, timeout: int = 15) -> None:
        self.api_key = api_key
        self.client_code = client_code
        self.password = password
        self.totp_code = totp_code
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()

    def _headers(self) -> Dict[str, str]:
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-PrivateKey': self.api_key,
        }

    def create_session(self) -> SmartApiSession:
        """Create broker session.

        Keep this conservative until exact production payload/response fields are
        verified from your SmartAPI docs/account setup.
        """
        raise NotImplementedError('SmartAPI create_session wiring pending exact verified request/response contract.')

    def refresh_session(self, refresh_token: str) -> SmartApiSession:
        raise NotImplementedError('SmartAPI refresh_session wiring pending exact verified request/response contract.')
