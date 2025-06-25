import requests
from dotenv import load_dotenv
import argparse

load_dotenv()

cmdparser = argparse.ArgumentParser(
    description="pyhjonk user.py - View posts from a user.",
    epilog="usage: py user.py [-h] [args] username"
)

cmdparser.add_argument("username", type=str, default=1, help="Selects username")
cmdparser.add_argument("-p", "--page", type=int, default=1, help="Selects page (Default: 1)")
cmdparser.add_argument("-r", "--rows", type=int, default=10, help="Selects amounts of rows to get (Default: 10)")
cmdargs=cmdparser.parse_args()

url = "https://hjonk.me"

posts = requests.get(f"{url}/api/v1.0/posts/{cmdargs.username}?lim={cmdargs.rows}&page={cmdargs.page}")

for item in posts.json():
    if item['replying_to'] is not None:
        print(f"\033[95mPosted at {item['created_at']}, Replying to {item['replying_to']}\033[0m")
    else:
        print(f"\033[95mPosted at {item['created_at']}\033[0m")

    print(f"{item['body']}")
    mediaCounter = -1
    if item['media'] is not None:
        for media in item['media']:
            mediaCounter += 1
            print(f"{media['type'].capitalize()}: {url}/cdn/attachment/{item['id']}/{mediaCounter}")
    if item['associated_post'] is not None:
        print(f"Associated post: {url}/@ignorethis/{item['associated_post']}")
    print("")