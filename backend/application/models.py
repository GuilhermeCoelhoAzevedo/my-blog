from app import db, ma
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

class Article(db.Model):
    __tablename__ = 'Article'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    upVotes = Column(Integer)

class Comment(db.Model):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key = True)
    article_id = Column(Integer, ForeignKey('Article.id'))
    username = Column(String)
    text = Column(String)
    
class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'upVotes')

class CommentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'article_id', 'username', 'text')

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)

comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)