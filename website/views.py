# for url endpoints

from flask import Blueprint 

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/home')
def home():
    return("<h1> Home Page </h1>")