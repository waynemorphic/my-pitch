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
    email = StringField('YOUR EMAIL ADDRESS', validators=[InputRequired(), Email()])
    password = PasswordField('PASSWORD', validators=[InputRequired()])
    submit = SubmitField('Login')
    remember = BooleanField('Remember Me')

class RegistrationForm(FlaskForm):
    '''
    class for identifying registration form
    '''
    username = StringField('YOUR USERNAME', validators=[InputRequired(), Length(min=3, max=20)])
    email = StringField('YOUR EMAIL ADDRESS', validators=[InputRequired(), Email()])
    password = PasswordField('PASSWORD', validators=[InputRequired()])
    confirm_password = PasswordField('CONFIRM PASSWORD', validators=[InputRequired(), EqualTo('PASSWORD')])
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
    comment = StringField('Leave a Comment')
    submit = SubmitField('Post')

class PitchForm(FlaskForm):
    '''
    class defines user pitches posted on the platform
    '''
    category = StringField('INDUSTRY/SECTOR CATEGORY i.e Tech, Agriculture ...')
    pitch = TextAreaField('YOUR PITCH', validators=[InputRequired(), Length(min=20)])
    submit = SubmitField('Post Pitch')
    