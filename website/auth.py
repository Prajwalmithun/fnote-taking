# 
from crypt import methods
import email
from nis import cat
from flask import Blueprint, render_template, request,flash 
from .input_validation import *

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"



@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():
    # we are diff GET and POST request
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # check if we are grabbing the values from UI correctly
        #print(email,firstName,password1,password2)

        # basic checks, and flash for showing messages on UI
        # email length check
        if len(email) < 4:
            flash ('Email must be greater than 4 characters', category='error')
        # firstname check
        # 1. length
        # 2. shouldnt start with numbers or special chrs
        elif len(firstName) < 3:
            flash('Fist Name must be greater than 3 characters',category='error')
        # password check
        # 1. min length = 8
        # 2. 1 uppercase 1 lowercase 1 specialchr
        elif len(password1) < 7:
            flash("Password must be at least 7 characters",category='error')
        elif not contains_chr(password1):
            flash("Password must contains at least 1 special characters",category='error')
        elif not contains_upper(password1):
            flash("Password must contain atleast 1 uppercase letter",category="error")
        elif not contains_lower(password1):
            flash("Password must contain atleast 1 lowercase alphabet",category="error")
        elif password1 != password2:
            flash("Password not maching",category='error')
        else:
            flash("User created",category='success')

    return render_template("sign_up.html")