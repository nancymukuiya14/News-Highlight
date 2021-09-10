from flask import render_template
from .request import get_news_source, get_article
from app import app

@app.route('/')
def index():
    results = get_news_source()
    return render_template('index.html', results = results)

@app.route('/news/<id>')
def news(id):
    article = get_article(id)
    print(article)
    return render_template('article.html',article =article)
