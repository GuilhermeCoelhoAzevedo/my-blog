from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__, static_folder='frontend/my-blog/build', static_url_path='')

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://')

db = SQLAlchemy(app)
ma = Marshmallow(app) 

from backend.application import routes
from backend.application import models