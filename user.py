import requests
from bs4 import BeautifulSoup

base_url = "https://hjonk.me"

username = input("Enter the username of the user you want the posts from: ")
print("You chose to view posts from", username)

response = requests.get(f"{base_url}/profile/feed?user={username}")

# Stuff to parse HTML
soup = BeautifulSoup(response.content, 'html5lib')

posts_text_raw = soup.find_all("div", class_="text")

for posts_text in posts_text_raw:
    print(posts_text.text)
