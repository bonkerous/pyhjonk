import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

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

response = session.get(f"{url}/profile/feed?user={username}")

# Stuff to parse HTML
soup = BeautifulSoup(response.content, 'html5lib')

posts_text_raw = soup.find_all("div", class_="text")

for posts_text in posts_text_raw:
    print(posts_text.text)
