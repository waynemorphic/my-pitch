from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, BooleanField # |boolean renders checkbox in our form
from wtforms.validators import InputRequired,Email,EqualTo
# from ..models import User
from wtforms import ValidationError

# login a user with existing credentials
class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[InputRequired(),Email()])
    password = PasswordField('Password',validators =[InputRequired()])
    remember = BooleanField('Remember me') # boolean to confirm wheter the user wants to be logged out after the session.
    submit = SubmitField('Sign In')