# to treate the current directory as package

from flask import Flask

# flask app initialization
def create_app():
    app = Flask(__name__)
    
    # encrypt the session data and cookies
    app.config['SECRET_KEY'] = 'afsdhjksfadkjsfajhfajh'

    # register the endpoints
    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')


    return app