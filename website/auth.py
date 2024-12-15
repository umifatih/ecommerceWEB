from flask import Blueprint, render_template
from .forms import LoginForm, SignUpForm

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return 'ini halaman login'

@auth.route('/sign-up')
def sign_up():
    form = SignUpForm()
    
    return render_template('signup.html', form=form)


