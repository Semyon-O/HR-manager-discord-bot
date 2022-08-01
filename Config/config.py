import json


def get_token() -> str:
    with open('Config/config.json') as config:
        cfg = json.load(config)
        token_bot = cfg["token"]
    return token_bot


TOKEN = get_token()