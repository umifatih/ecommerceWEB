from flask import Blueprint 

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return 'ini halaman login'

@auth.route('/sign-up')
def sign_up():
    return 'ini halaman sign up'


