import feedparser

def main():
    feedList = ['https://justthenews.com/rss.xml', 'https://nypost.com/feed/']
    feeds = map(feedparser.parse, feedList)
    for feed in feeds:
        for entry in feed['entries']:
            print(entry['title'])

if __name__ == '__main__':
    main()
