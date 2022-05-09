from flask import Flask, render_template, flash, redirect, url_for
# from application import app
from . import main
# from models import User, Comment
from application.auth.forms import LoginForm, PitchForm, RegistrationForm, CommentForm

# secret_key = app.config['SECRET_KEY']

@main.route('/posts')
def posts():
    '''
    functions defines view for posted pitches by other users
    '''
    title = 'MYPITCH'
    form = CommentForm()
    pitch = PitchForm()
    return render_template('posts.html', title = title, form = form, pitch = pitch)

# login page
@main.route('/', methods=['GET', 'POST'])
def login():
    '''
    login function allows a user to either login or redirect to app registration
    '''
    
    title = 'MYPITCH'
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login Successful. Welcome to MYPITCH", 'message')
        print("he")
        return redirect(url_for('posts'))
       
    else:
        return render_template('auth/login.html', title = title, form = form)

@main.route('/register', methods=['GET', 'POST'])
def register():
    '''
    user registration function
    '''
    
    title = 'MYPITCH'
    form = RegistrationForm()
    if form.validate_on_submit():
        flash("Registration Successful. Welcome to MYPITCH", 'message')
        print("he")
        # return redirect(url_for('posts'))
    return render_template('auth/register.html', title = title, form = form)


