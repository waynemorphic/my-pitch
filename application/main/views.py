from urllib import request
from flask import Flask, render_template, flash, redirect, url_for
from ..models import Users
# from application import app
from . import main
from application.auth.forms import LoginForm, PitchForm, RegistrationForm, CommentForm
from flask_login import login_required, login_user, logout_user
from application import db

# secret_key = app.config['SECRET_KEY']

@main.route('/posts')
@login_required # authenticating that the user is logged before accessing the posts
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
        user = Users.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.email.data):
            login_user(user, form.remember.data)
            return redirect(request.args.get('next') or url_for('main.posts'))
        flash("Login Successful. Welcome to MYPITCH", 'message')
    
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
        user = Users (email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit(user)
        
        flash("Registration Successful. Welcome to MYPITCH", 'message')
        print("he")
        # return redirect(url_for('posts'))
    return render_template('auth/register.html', title = title, form = form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.login"))
