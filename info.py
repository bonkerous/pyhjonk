import requests
from dotenv import load_dotenv
import os
import json
import argparse

load_dotenv()

cmdparser = argparse.ArgumentParser(
    description="pyhjonk info.py - View information about a user.",
    epilog="usage: py info.py [-h] [args] username"
)

cmdparser.add_argument("username", type=str, default=1, help="Selects username")
cmdargs=cmdparser.parse_args()

url = "https://hjonk.me"

user = requests.get(f"{url}/api/v1.0/user/{cmdargs.username}")

for item in user.json():
    print(f"{item}")