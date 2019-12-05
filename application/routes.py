from flask import Flask, render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import User
from application.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        print('a')
        return redirect(url_for('home'))

    form = LoginForm()
    if form.validate_on_submit():
        print('b')
        user=User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            print('c')
            next_page = request.args.get('next')

            if next_page:
                print('d')
                return redirect(next_page)
            else:
                print('e')
                return redirect(url_for('home'))
            print('f')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/pokemonpage')
def pokemonpage():
    return render_template('pokemonpage.html', title='Pokemon Page')

@app.route('/fastmovespage')
def fastmovespage():
    return render_template('fastmovespage.html', title='Fast Moves Page')

@app.route('/chargemovespage')
def chargemovespage():
    return render_template('chargemovespage.html', title='Charge Moves Page')
