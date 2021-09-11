from app.models import Articles
from flask import render_template
from . import main
from ..request import get_articles_category, get_news_source, get_article


@main.route('/')
def index():
    results = get_news_source()
    articles = get_articles_category('entertainment') 
    return render_template('index.html', results = results, articles = articles)

@main.route('/news/<id>')
def news(id):
    article = get_article(id)
    print(article)
    return render_template('article.html',article =article)

@main.route('/category')
def category(category):
    article = get_articles_category(category)
    print(article)
    return render_template('category.html')
