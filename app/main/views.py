from flask import render_template
from . import main
from ..request import get_news_source, get_article


@main.route('/')
def index():
    results = get_news_source()
    return render_template('index.html', results = results)

@main.route('/news/<id>')
def news(id):
    article = get_article(id)
    print(article)
    return render_template('article.html',article =article)

