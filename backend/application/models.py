# backend/application/models.py
from app import db, ma


# ---------------------------
# MODELS
# ---------------------------

class Article(db.Model):
    __tablename__ = 'Article'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    upVotes = db.Column(db.Integer, default=0)

    # Comments relationship
    comments = db.relationship('Comment', backref='article', lazy=True)

    def __repr__(self):
        return f"<Article {self.name}>"


class Comment(db.Model):
    __tablename__ = 'Comment'

    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey('Article.id'), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    text = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Comment {self.username}: {self.text[:20]}>"


# ---------------------------
# SCHEMAS
# ---------------------------

class ArticleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Article
        load_instance = True
        include_relationships = True
        include_fk = True


class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        load_instance = True
        include_fk = True


# ---------------------------
# SCHEMA INSTANCES
# ---------------------------

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)

comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)
