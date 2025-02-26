import requests

base_url = "https://hjonk.me"

username = input("Enter the username of the user you want the posts from: ")
print("You chose to view posts from", username)

responce = requests.get(f"{base_url}/profile/feed?user={username}")
print(responce.content)
