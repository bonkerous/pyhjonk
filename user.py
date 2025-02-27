import requests
from bs4 import BeautifulSoup

base_url = "https://hjonk.me"
session = requests.Session()

payload = {'handle': "YOURHANDLE", 'password': "YOURPASSWORD"}

session.post(f"{base_url}/auth/login", data=payload)

print(session)

username = input("Enter the username of the user you want the posts from: ")
print("You chose to view posts from", username)

response = session.get(f"{base_url}/profile/feed?user={username}")

# Stuff to parse HTML
soup = BeautifulSoup(response.content, 'html5lib')

posts_text_raw = soup.find_all("div", class_="text")

for posts_text in posts_text_raw:
    print(posts_text.text)
