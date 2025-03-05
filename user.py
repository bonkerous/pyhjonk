import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

url = "https://hjonk.me"
session = requests.Session()
payload = {'handle': os.getenv('HANDLE'), 'password': os.getenv('PASSWORD')}

login = session.post(f"{url}/auth/login", data=payload)
if login.status_code == 200:
    print("Successfully logged in!")
    pass
else:
    print("Are you sure your credentials are correct?")

username = input("Enter the username of the user you want the posts from: ")
print(f"You chose to view posts from {username}")

posts = session.get(f"{url}/api/v1.0/posts/{username}")

for item in posts.json():
    print(f"{item['body']} (posted at {item['created_at']})")
