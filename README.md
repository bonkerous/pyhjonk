## pyhjönk

suite of cli python apps to interact with [hjonk.me](https://hjonk.me)

**WARNING: THIS IS VERY VERY SHIT SOFTWARE NOT READY FOR REAL WORLD USE LOLOLOL**

## how to use

Install dependencies
```
pip install requests bs4 html5lib
```

Run the thin
```
python3 user.py
```

Edit user.py to have handle and password for login

```
payload = {'handle': "YOURHANDLE", 'password': "YOURPASSWORD"}
                        ^^^^^^^                  ^^^^^^^^^^
```
(this will be better by using a config file soon...)
