from __future__ import annotations

import os
import sys
from pprint import pprint

from dotenv import load_dotenv


def fail(message: str) -> None:
    print(f'ERROR: {message}')
    sys.exit(1)


def main() -> None:
    load_dotenv()

    client_id = os.getenv('ANGEL_CLIENT_ID', '').strip()
    api_key = os.getenv('ANGEL_API_KEY', '').strip()
    pin = os.getenv('ANGEL_PIN', '').strip()
    totp_secret = os.getenv('ANGEL_TOTP_SECRET', '').strip()

    missing = [
        name
        for name, value in [
            ('ANGEL_CLIENT_ID', client_id),
            ('ANGEL_API_KEY', api_key),
            ('ANGEL_PIN', pin),
            ('ANGEL_TOTP_SECRET', totp_secret),
        ]
        if not value
    ]
    if missing:
        fail(f'Missing required env values: {", ".join(missing)}')

    from .engines.smartapi_sdk import SmartApiCredentials, SmartApiSdkAdapter

    adapter = SmartApiSdkAdapter(
        SmartApiCredentials(
            api_key=api_key,
            client_code=client_id,
            pin=pin,
            totp_secret=totp_secret,
        )
    )

    print('Creating SmartAPI session...')
    response = adapter.create_session()

    if not response:
        fail('Empty response from SmartAPI generateSession')

    print('Login response keys:')
    print(sorted(list(response.keys())))

    data = response.get('data') or {}
    safe_output = {
        'status': response.get('status'),
        'message': response.get('message'),
        'has_data': bool(data),
        'has_jwtToken': bool(data.get('jwtToken')),
        'has_refreshToken': bool(data.get('refreshToken')),
        'feed_token_from_method': bool(adapter.get_feed_token()),
    }
    pprint(safe_output)


if __name__ == '__main__':
    main()
