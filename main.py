from flask import Flask, request, jsonify, render_template
import feedparser

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        print(request.form.getlist('feedname'))

    return render_template('index.html')

@app.route('/feed')
def load_feed(feed_list):
    feeds = map(feedparser.parse, feedList)
    titles = []
    for feed in feeds:
        for entry in feed['entries']:
            titles.append(entry['title'])
    return jsonify(titles)

if __name__ == '__main__':
    app.run()
