import requests
import json

def get_token(id: str, secret: str, region: str) -> str:
    try:
        return json.loads(
            requests.post(
            url='https://www.battlenet.com.cn/oauth/token' if region == 'cn'
                else 'https://oauth.battle.net/token',
            auth=(id, secret), # type: ignore
            data={'grant_type': 'client_credentials'},
            ).content
        )['access_token']
    except requests.exceptions.ConnectionError as e:
         exit(f'{e}.')