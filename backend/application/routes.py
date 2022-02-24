from re import L
from app import app, db
from flask import jsonify, render_template, request
from flask.helpers import send_from_directory
from backend.application.models import *

def json_definition(article):
    result = article_schema.dump(article)
    comments = Comment.query.filter_by(article_id=article.id).all()
    result["comments"] = comments_schema.dump(comments)

    return result

############# 
#React routes
############# 
"""
@app.route('/', methods=['GET'])
def serve():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/about', methods=['GET'])
def about():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/articles-list', methods=['GET'])
def articles_list():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/article/<string:name>', methods=['GET'])
def article(name: str):
    return send_from_directory(app.static_folder, 'index.html')
"""
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return send_from_directory(app.static_folder, 'index.html')

############# 
#API routes
############# 
@app.route('/api/article/<string:name>', methods=['GET'])
def api_articles(name: str):
    article = Article.query.filter_by(name=name).first()

    if article:
        return jsonify(json_definition(article))
    else:
        return jsonify(message="Article doesn't exist"), 404

@app.route('/api/articleUpVote/<string:name>', methods = ['POST'])
def articleUpVote(name: str):
    article = Article.query.filter_by(name=name).first()

    if article:
        article.upVotes += 1
        db.session.commit()
        
        return jsonify(json_definition(article))
    else:
        return jsonify(message="Article doesn't exist"), 404

@app.route('/api/addComment/<string:name>', methods = ['POST'])
def AddComment(name: str):

    article = Article.query.filter_by(name=name).first()

    if article:
        username = request.json['username']
        text = request.json['text']

        comment = Comment(username=username,text=text, article_id=article.id)
        db.session.add(comment)
        db.session.commit()

        return jsonify(json_definition(article))
    else:
        return jsonify(message="Article doesn't exist"), 404

##################
#Database commands
##################
@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Database created!')

@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database dropped!')

@app.cli.command('db_seed')
def db_seed():
    article1 = Article(
        name="learn-react",
        upVotes=0
    )

    article2 = Article(
        name="learn-node",
        upVotes=0
    )

    article3 = Article(
        name="my-thoughts-on-resumes",
        upVotes=0
    )

    comment1 = Comment(
        article_id = 1,
        username="George",
        text = "Nice article!"
    )

    comment2 = Comment(
        article_id = 1,
        username="Dimitry",
        text = "Very interesting!"
    )

    db.session.add(article1)
    db.session.add(article2)
    db.session.add(article3)
    db.session.add(comment1)
    db.session.add(comment2)
    db.session.commit()

    print("Database seeded!")
