import os
import subprocess
import requests
import tempfile
from dotenv import load_dotenv

load_dotenv()

url = "https://hjonk.me"
session = requests.Session()
loginPayload = {'handle': os.environ.get('HANDLE'), 'password': os.environ.get('PASSWORD')}

temp = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
temp_filename = temp.name

if os.environ.get('EDITOR') is not None:
    subprocess.call([os.environ['EDITOR'],temp_filename])
else:
    print("NO EDITOR SET! Please set an editor either via setting the EDITOR environment variable, or in the .env file!")
    print("Exiting.")
    quit()
with open(temp_filename) as postText:
    print(postText.read())

    userConfirmPost = input("Do you want to post this? [y/N] ")

    if userConfirmPost == 'y':
        print("Logging in...")
        login = session.post(f"{url}/auth/login", data=loginPayload)
        if loginStatus == 200:
            print("Logged in successfully!")
            session.post(f"{url}/post/post", data=postText.read())
        else:
            print("Login failed, check your credentials.")
            quit()
    else:
        print("Exiting.")
        quit()
