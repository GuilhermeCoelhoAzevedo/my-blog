from app import db
from backend.application.models import *

db.create_all()

article1 = Article(
    name="learn-react",
    upVotes=5
)

article2 = Article(
    name="learn-node",
    upVotes=6
)

article3 = Article(
    name="my-thoughts-on-resumes",
    upVotes=10
)

db.session.add(article1)
db.session.add(article2)
db.session.add(article3)
db.session.commit()