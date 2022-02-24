from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__, static_folder='frontend/my-blog/build', static_url_path='')

#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://yhodyuskgjilmv:7b0315ff3f4e7c0faa3a94811450cb6e1d05f62b1266bea952bd3f810eaa35e8@ec2-34-247-151-118.eu-west-1.compute.amazonaws.com:5432/dcasvbhf0ljehf'

db = SQLAlchemy(app)
ma = Marshmallow(app) 

from backend.application import routes
from backend.application import models