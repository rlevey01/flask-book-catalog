from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.auth.models import User

def user_name_exists(form, field):
    user_name = User.query.filter_by(user_name=field.data).first()
    if user_name:
        raise ValidationError('User Name Already Exists')


def email_exists(form, field):
    email = User.query.filter_by(user_email=field.data).first()
    if email:
        raise ValidationError('Email Already Exists')

class RegistrationForm(FlaskForm):
    name = StringField('Whats your Name', validators=[DataRequired(),  Length(3,15, message='between 3 to 15 characters'),user_name_exists])
    email = StringField('Enter your E-mail',validators=[DataRequired(), Email(), email_exists])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm = PasswordField('Confirm', validators=[DataRequired()])

    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(5), EqualTo('confirm', message='password must match')])
    confirm = PasswordField('Confirm', validators=[DataRequired()])
    stay_loggedin = BooleanField('stay logged-in')
    submit = SubmitField('Login')

