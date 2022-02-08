# 
from crypt import methods
import email
from nis import cat
from flask import Blueprint, render_template, request,flash 

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
        if len(email) < 4:
            flash ('Email must be greater than 4 characters', category='error')
        elif len(firstName) < 3:
            flash('Fist Name must be greater than 3 characters',category='error')
        elif len(password1) < 7:
            flash("Password must be at least 7 characters",category='error')
        elif password1 != password2:
            flash("Password not maching",category='error')
        else:
            flash("User created",category='sucess')

    return render_template("sign_up.html")