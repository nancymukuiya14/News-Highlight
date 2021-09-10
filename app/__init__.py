from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
from app import views

Bootstrap = Bootstrap()

# Initializing application
app = Flask(__name__)

# Setting up configuration
app.config.from_object(DevConfig)

views.init_app(app)

