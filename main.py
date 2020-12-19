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
    return render_template('feed.html', feeds=feeds)

if __name__ == '__main__':
    app.run()
