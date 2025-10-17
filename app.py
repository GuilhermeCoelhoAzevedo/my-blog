from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#App initilization - Using React build
app = Flask(__name__, static_folder='frontend/my-blog/build', static_url_path='')

#App initilization - Development (Just Flask API)
#app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://')

db = SQLAlchemy(app)
ma = Marshmallow(app) 

from backend.application import routes
from backend.application import models