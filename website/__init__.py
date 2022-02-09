# to treate the current directory as package

from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # for database
from os import path

# creating database object
db = SQLAlchemy()
DB_NAME = "database.db"


# flask app initialization
def create_app():
    app = Flask(__name__)
    
    # encrypt the session data and cookies
    app.config['SECRET_KEY'] = 'afsdhjksfadkjsfajhfajh'

    # configuration database
    # we are using sqlite (basically a file that stores the data)
    app.config['SQL_ALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    print(app.config['SQL_ALCHEMY_DATABASE_URI'])
    # database initialising for our app (ie., informing our app to use this database)
    db.init_app(app)

    # importing the blueprints(or endpoints)
    from .views import views
    from .auth import auth

    # register the blueprints(or endpoints)
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import User, Note
    create_database(app)

    return app

# create database if DB doesnt exits
def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Database created")