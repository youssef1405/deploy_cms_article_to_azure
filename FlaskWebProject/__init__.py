"""
The flask application package.
"""
import logging
import sys
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)

# TODO: Add any logging levels and handlers with app.logger

handler = logging.StreamHandler(stream=sys.stdout)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

# app.logger.setLevel(logging.INFO)
# streamHandler = logging.StreamHandler(stream=sys.stdout)
# streamHandler.setLevel(logging.INFO)
# app.logger.addHandler(streamHandler)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
