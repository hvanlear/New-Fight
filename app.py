from flask import Flask, request, jsonify, render_template
from util import NewsData

from models import db, connect_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///news_fight_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)


@app.route('/')
def home():
    # possibly call class methods in jinja?
    fox_stories = NewsData('foxnews.com').getArticles()
    cnn_stories = NewsData('cnn.com').getArticles()
    sources = NewsData().getSources()
    return render_template('home.html', fox_stories=fox_stories,
                           cnn_stories=cnn_stories, sources=sources)


@app.route('/search', methods=['GET', 'POST'])
def updated_search():
    if request.method == 'POST':
        req = request.form
        topic = req.get('topic_search')
        lsource = req.get('left_sources')

    fox_stories = NewsData('foxnews.com', topic).getArticles()
    cnn_stories = NewsData('cnn.com', topic).getArticles()

    return render_template('home.html', fox_stories=fox_stories, cnn_stories=cnn_stories)

# Load all elements via JS
