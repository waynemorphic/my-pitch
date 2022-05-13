from email import contentmanager
from urllib import request
from flask import Flask, render_template, flash, redirect, url_for, abort
from ..models import Users, Pitch, Comment, Upvote, Downvote
# from application import app
from . import main
from application.auth.forms import LoginForm, PitchForm, RegistrationForm, CommentForm, UpdateProfile
from flask_login import login_required, login_user, logout_user, current_user
from application import db, photos

# secret_key = app.config['SECRET_KEY']

@main.route('/posts')
# @login_required # authenticating that the user is logged before accessing the posts
def posts():
    '''
    functions defines view for posted pitches by other users
    '''
    title = 'MYPITCH'
    
    posts = Pitch.query.all() 
    
    return render_template('posts.html', title = title, posts = posts)

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
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember.data)
            return redirect( url_for('main.posts'))
        flash("Invalid Username or Password", 'danger')
       
 
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
        db.session.commit()
        
        flash("Registration Successful. Welcome to MYPITCH", 'message')
        
        return redirect(url_for('main.login'))
    return render_template('auth/register.html', title = title, form = form)


@main.route('/posts/addpitch', methods = ['GET', 'POST'])
@login_required
def add_pitch():
    '''
    adding a pitch
    '''
    
    title = 'MYPITCH'
    user = Users.query.first()
    pitch = PitchForm()
   
    if pitch.validate_on_submit():
        add_pitch = Pitch(category_stuff = pitch.category_stuff.data, pitch_stuff = pitch.pitch_stuff.data )
        
        add_pitch.save_pitch()
        
        flash("Pitch posted!", "success")
        
        return redirect(url_for('main.posts'))
    # pitched = Pitch.get_user_pitch()
    return render_template('add_pitch.html', title = title, pitch = pitch)

@main.route('/posts/comment/new/int:<pitch_id>', methods = ['GET', 'POST'])
@login_required
def add_comment(pitch_id):
    '''
    adds comment to a post
    '''
    
    pitch = Pitch.query.filter_by(id = pitch_id).first().pitch_stuff

    # pitch = Pitch.query.get(pitch_id)
    print(pitch)
    form = CommentForm()
    
    
    # all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    
    # all_comments = Comment.get_comment(pitch_id)

    if form.validate_on_submit():
        # pitch_id = pitch_id 
        # user_id = current_user._get_current_object().id
        
        # added_comment = Comment(comment_stuff = form.comment_stuff.data, user_id = user_id, pitch_id = pitch_id)
        added_comment = Comment(comment_stuff = form.comment_stuff.data, user = current_user, pitch_id = pitch_id)

        added_comment.save_comment()
        
        flash('Comment added successfully', 'success')
        return redirect(url_for('main.add_comment', pitch_id = pitch_id))
    
    all_comments = Comment.get_comment(pitch_id)
    print(all_comments)

    return render_template('comment.html', form = form, all_comments = all_comments, pitch = pitch)


@main.route('/user/<uname>')
def profile(uname):
    '''
    user profile method
    '''
    user = Users.query.filter_by(username = uname).first()
    title = current_user.username
    
    if user is None:
        abort(404)
    
    
    return render_template('profile/profile.html', user = user, title = title)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = Users.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = Users.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/like/<int:id>', methods = ['GET', 'POST'])
def upvotes(id):
    like_vote = Upvote.get_upvote(id)
    valid_string = f'{current_user.id}:{id}'
    
    for like in like_vote:
        to_str = f'{like}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.posts'))
        
        else:
            continue
    new_like_upvote = Upvote(user = current_user, pitch_id = id)
    new_like_upvote.save_upvote()
    return redirect(url_for('main.posts'))

@main.route('/dislike/<int:id>', methods = ['GET', 'POST'])
def downvotes(id):
    dislike_vote = Downvote.get_downvote(id)
    valid_string = f'{current_user.id}:{id}'
    
    for dislike in dislike_vote:
        to_str = f'{dislike}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.posts'))
        
        else:
            continue
    new_dislike_vote = Downvote(user = current_user, pitch_id = id)
    new_dislike_vote.save_downvote()
    return redirect(url_for('main.posts'))

# @main.route('/posts/<category_id>')
# def pitch_category(category_id):
#     '''
#     pitch category method
#     '''
    
#     Tech = Pitch.query.filter_by(title = 'Tech').all()
#     Marketing = Pitch.query.filter_by(title = 'Marketing').all
#     Sport = Pitch.query.filter_by(title = 'Sport').all
#     General = Pitch.query.filter_by(title = 'General').all
#     pitches = Pitch.query.all()
#     # category = Category.query.filter_by(id = category_id).first()
#     # the_category = Category.the_category
#     # categories = Category.query.all()
#     # comments = Comment.query.all()
#     return render_template('category.html', Tech = Tech, Marketing = Marketing, Sport = Sport, General = General,  pitches = pitches)
    
@main.route('/logout')
# @login_required
def logout():
    logout_user()
    return redirect(url_for("main.login"))


# https://drive.google.com/file/d/1vfIR_EoPZRbB0BW_ESJuqLo1n1h4vkp-/view