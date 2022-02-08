# for url endpoints

from flask import Blueprint, render_template

# Creating a blueprint
# syntax: Blueprint(<name of the view>,__name__)
views = Blueprint('views', __name__)


# decorators
# for specifying the routes
@views.route('/')
@views.route('/home')
def home():
    return render_template("home.html")