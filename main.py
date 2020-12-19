from flask import Flask, request, render_template
import feedparser

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/feed', methods=['GET', 'POST'])
def load_feed():
    feed_list = []
    if request.method == 'POST':
        feed_list = request.form.getlist('feedname')

    feeds = map(feedparser.parse, feed_list)
    titles = []
    for feed in feeds:
        for entry in feed['entries']:
            titles.append(entry['title'])
    return render_template('feed.html', titles=titles)

if __name__ == '__main__':
    app.run()
