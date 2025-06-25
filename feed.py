import feedparser

url = ("https://hjonk.me/rss/feed")
feed = feedparser.parse(url)

if feed.status == 200:
    for entry in feed.entries:
        print(f"Posted on {entry.published}")
        if entry.description == "":
            print("\033[91mNothing, probably a repost or an embed.\033[0m")
        else:
            print(entry.description)
        print(f"Link: {entry.link}")
        print("")
else:
    print("Failed to get RSS feed. Status code:", feed.status)