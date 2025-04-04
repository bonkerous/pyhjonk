import requests
from dotenv import load_dotenv
import os
import json
import argparse

load_dotenv()

cmdparser = argparse.ArgumentParser(
    description="pyhjonk user.py - View posts from a user.",
    epilog="usage: py [-h] [args] username"
)

cmdparser.add_argument("username", type=str, default=1, help="Selects username")
cmdparser.add_argument("-p", "--page", type=int, default=1, help="Selects page (Default: 1)")
cmdparser.add_argument("-r", "--rows", type=int, default=10, help="Selects amounts of rows to get (Default: 10)")
cmdargs=cmdparser.parse_args()

url = "https://hjonk.me"

posts = requests.get(f"{url}/api/v1.0/posts/{cmdargs.username}?lim={cmdargs.rows}&page={cmdargs.page}")

for item in posts.json():
    print(f"{item['body']} (posted at {item['created_at']})")
