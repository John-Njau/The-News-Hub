from flask import render_template,request,redirect,url_for
from ..requests import get_source, get_news_articles, search_news, get_articles_category
from . import main

@main.route('/')
def index():
    title = "NewsHub"
    sources = get_source()
    search_news = request.args.get('news_query')
    if search_news:
        return redirect(url_for('.search',phrase=search_news))
    else:
        return render_template('index.html', title=title, sources=sources)

@main.route('/news/<id>')
def articles(id):
    title = "News Articles"
    articles = get_news_articles(id)
    return render_template('articles.html' , articles=articles, title=title)

@main.route('/news/<phrase>')
def search(phrase):
    phrase_list = phrase.split(" ")
    phrase_format = "+".join(phrase_list)
    searched_phrase = search_news(phrase_format)
    title = f'Results for {phrase}'
    return render_template('search.html', news = searched_phrase, title = title)

# business/technology/sports /science
@main.route('/business')
def business():
    title = 'Business News'
    articles = get_articles_category('business')
    return render_template('business.html', title = title, articles = articles)

@main.route('/technology')
def technology():
    title = 'Tech News'
    articles = get_articles_category('technology')
    return render_template('technology.html', title = title, articles = articles)

@main.route('/sports')
def sports():
    title = 'Sports News'
    articles = get_articles_category('sports')
    return render_template('sports.html', title = title, articles = articles)

@main.route('/science')
def science():
    title = 'Science News'
    articles = get_articles_category('science')
    return render_template('science.html', title = title, articles = articles)