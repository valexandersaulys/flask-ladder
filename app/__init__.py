from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy  # alternatively, flask.ext.mongoengine
import os
from config import BASEDIR
from flask_wtf.csrf import CsrfProtect

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
CsrfProtect(app)  # necesary for protecting against CSRF, automatic in wtforms


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
There seems to be an implication here that blueprints can live just beneath the 
BASEDIR as opposed to underneath the BASEDIR/app directory. I'm not sure though
"""
from app import views, models
