from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from wtforms import ValidationError
from ..models import Users

class LoginForm(FlaskForm):
    '''
    class for identifying login fields
    '''
    email = StringField('Email Address', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')
    remember = BooleanField('Remember Me')

class RegistrationForm(FlaskForm):
    '''
    class for identifying registration form
    '''
    username = StringField('Username', validators=[InputRequired(), Length(min=3, max=20)])
    email = StringField('Email Address', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    # confirm_password = PasswordField('CONFIRM PASSWORD', validators=[InputRequired(), EqualTo('PASSWORD')])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired()])

    submit = SubmitField('Sign up')
    
    # validating new users registering in the platform
    def validate_email(self,data_field):
        if Users.query.filter_by(email =data_field.data).first():
            raise ValidationError('Account with that email exists')

    def validate_username(self,data_field):
        if Users.query.filter_by(username = data_field.data).first():
            raise ValidationError('Username is taken')
    
class CommentForm(FlaskForm):
    '''
    class for taking user comments purposefuly as pitch feedback
    '''
    comment_stuff = StringField('Leave a Comment')
    submit = SubmitField('Post')

class PitchForm(FlaskForm):
    '''
    class defines user pitches posted on the platform
    '''
    category_stuff = StringField('Category i.e Tech, Marketing....')
    pitch_stuff = TextAreaField('Enter Pitch', validators=[InputRequired(), Length(min=20)])
    submit = SubmitField('Post Pitch')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')