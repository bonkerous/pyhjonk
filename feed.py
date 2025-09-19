import requests
import argparse

cmdparser = argparse.ArgumentParser(
    description="pyhjonk feed.py - View feed.",
    epilog="usage: py feed.py [-h] [args]"
)

cmdparser.add_argument("-p", "--page", type=int, default=1, help="Selects page (Default: 1)")
cmdparser.add_argument("-r", "--rows", type=int, default=10, help="Selects amounts of rows to get (Default: 10)")
cmdargs=cmdparser.parse_args()

url = ("https://hjonk.me")
feed = requests.get(f"{url}/api/v1.0/feed?lim={cmdargs.rows}&page={cmdargs.page}")

for i in feed.json():
    if i['replying_to'] is not None:
        print(f"\033[95mPosted at {i['created_at']}, Replying to {i['replying_to']}\033[0m")
    else:
        print(f"\033[95mPosted at {i['created_at']}\033[0m")

    print(f"{i['body']}")

    mediaCounter = -1

    if i['media'] is not None:
        for media in i['media']:
            mediaCounter += 1
            print(f"{media['type'].capitalize()}: {url}/cdn/attachment/{i['id']}/{mediaCounter}")

    print("")