from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__, static_folder='frontend/my-blog', static_url_path='')
basedir = os.path.abspath(os.path.dirname(__file__))
    
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'myblog.db')

db = SQLAlchemy(app)
ma = Marshmallow(app) 

from backend.application import routes
from backend.application import models