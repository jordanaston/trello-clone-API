from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

def create_app():
    # using a list comprehension and multiple assignment 
    # to grab the environment variables we need
    
    # Creating the flask app object - this is the core of our app!
    app = Flask(__name__)

    # configuring our app:
    app.config.from_object("config.app_config")

    # creating our database object! This allows us to use our ORM
    db = SQLAlchemy(app)
    
    return app