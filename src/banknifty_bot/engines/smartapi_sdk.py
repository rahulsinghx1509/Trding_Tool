from __future__ import annotations

from dataclasses import dataclass
from importlib import import_module
from typing import Any, Dict, Optional

import pyotp


@dataclass
class SmartApiCredentials:
    api_key: str
    client_code: str
    pin: str
    totp_secret: str


class SmartApiSdkAdapter:
    """Thin adapter around the official SmartAPI Python SDK.

    This intentionally keeps broker-specific logic isolated from the rest of the bot.
    It uses TOTP from your local `.env` and expects the SmartAPI SDK to be installed
    in your runtime environment.
    """

    def __init__(self, credentials: SmartApiCredentials) -> None:
        self.credentials = credentials
        self._smart_connect = self._load_smart_connect()
        self.client = self._smart_connect(api_key=self.credentials.api_key)
        self.auth_payload: Dict[str, Any] = {}

    def _load_smart_connect(self):
        errors = []
        for module_name, attr_chain in [
            ('SmartApi', ['SmartConnect']),
            ('smartapi', ['SmartConnect']),
            ('smartapi.smartConnect', ['SmartConnect']),
        ]:
            try:
                module = import_module(module_name)
                obj = module
                for attr in attr_chain:
                    obj = getattr(obj, attr)
                return obj
            except Exception as exc:  # pragma: no cover - import-path compatibility
                errors.append(f'{module_name}: {exc}')
        joined = '; '.join(errors)
        raise ImportError(
            'Could not import SmartAPI SDK. Install the official SmartAPI Python package in your environment. '
            f'Import attempts: {joined}'
        )

    def generate_totp(self) -> str:
        return pyotp.TOTP(self.credentials.totp_secret).now()

    def create_session(self) -> Dict[str, Any]:
        totp_code = self.generate_totp()
        response = self.client.generateSession(
            self.credentials.client_code,
            self.credentials.pin,
            totp_code,
        )
        self.auth_payload = response or {}
        return self.auth_payload

    def get_feed_token(self) -> Optional[str]:
        try:
            return self.client.getfeedToken()
        except Exception:
            return None

    def get_ltp(self, exchange: str, tradingsymbol: str, symboltoken: str) -> Dict[str, Any]:
        return self.client.ltpData(exchange, tradingsymbol, symboltoken)

    def get_candles(self, historic_params: Dict[str, Any]) -> Dict[str, Any]:
        return self.client.getCandleData(historic_params)
