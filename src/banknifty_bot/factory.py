from .config import settings
from .engines.angel_one import AngelOneClient, AngelOneCredentials, AngelOneMarketDataProvider, PlaceholderNewsProvider
from .engines.market_data import DummyMarketDataProvider, DummyNewsProvider


def get_market_provider():
    provider_name = settings.market_data_provider.lower().strip()
    if provider_name == 'angel_one':
        credentials = AngelOneCredentials(
            api_key=settings.angel_api_key,
            client_id=settings.angel_client_id,
            pin=settings.angel_pin,
            totp_secret=settings.angel_totp_secret,
        )
        client = AngelOneClient(
            credentials=credentials,
            base_url=settings.angel_base_url,
            timeout=settings.http_timeout_seconds,
        )
        return AngelOneMarketDataProvider(client=client)
    return DummyMarketDataProvider()


def get_news_provider():
    provider_name = settings.news_provider.lower().strip()
    if provider_name == 'placeholder':
        return PlaceholderNewsProvider()
    return DummyNewsProvider()
