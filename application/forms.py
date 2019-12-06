from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import User
from flask_login import LoginManager, current_user

class RegistrationForm(FlaskForm):
    username = StringField('Username',
            validators=[
                DataRequired()
        ]
    )
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )
    confirm_password = PasswordField('Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password')
        ]
    )
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email is already in use!')


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('Username is already in use!')

class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class PokemonForm(FlaskForm):
    pokemon_name = StringField('Name',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ]
    )

    pokemon_fast = StringField('fast',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ]
    )

    pokemon_charge = StringField('charge',
        validators=[
            DataRequired(),
            Length(min=4, max=100)
        ]
    )

    submit = SubmitField('Post Content')
