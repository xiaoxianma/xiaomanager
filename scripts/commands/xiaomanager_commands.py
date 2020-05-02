import requests
from termcolor import cprint
from pprint import pprint
from nubia import argument, command

API_URL = "https://xiaomanager.herokuapp.com/api"


@command
@argument("user", description="xiaomanager username")
@argument("pwd", description="xiaomanager password")
def get_token(user: str, pwd: str):
    """
    exchange xiaomanager token
    """
    payload = {'username': user, 'password': pwd}
    url = f'{API_URL}/token/'
    res = requests.post(url, json=payload)
    if res.ok:
        pprint(res.json())
    else:
        cprint("Failed to get token", color='red')
