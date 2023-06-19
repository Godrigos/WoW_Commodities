import requests
import json
import sys

def get_item_id(url, locale, token, item:str = '') -> int:

    try:
        res = requests.get(
                f'{url}search/item?namespace=static-us'
                f"&name.{locale}={item}"
                f'&access_token={token}'
            )
        return json.loads(res.content)['results'][0]['data']['id']
    except requests.exceptions.ConnectionError as e:
        sys.exit(f'{e}.')