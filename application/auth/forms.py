from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, Length, Email, EqualTo

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