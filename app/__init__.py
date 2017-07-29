from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# alternatively, from flask_mongoengine import MongoEngine
import os
from config import BASEDIR

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
# db = MongoEngine(app) 

# User Authentication Dictionary (would be Redis-cache in production)
authhashes = {};

# --------------------- Logging Errors
import logging
from logging.handlers import RotatingFileHandler
file_handler = RotatingFileHandler("activities.log",maxBytes=100000,backupCount=1);
file_handler.setLevel(10);
app.logger.addHandler(file_handler);
app.logger.setLevel(level=0);
logger = app.logger


# ==================== Start the App !
"""
blueprints live just below the app/ folder as subfolders with a similar 
layout to the BASEDIR/app/ folder. 
>>> from app.simple_page import simple_page

>>> app.register_blueprint(simple_page)
and within BASEDIR/app/simple_page/__init__.py

>>> simple_page = Blueprint('simple_page, __name__, template_folder="templates")
Then add simple_page routing like in the BASEDIR/app/
"""
# I though below was >>> from app import views, models
import csrf_protect
import views, models
