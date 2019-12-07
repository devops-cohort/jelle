from flask import Flask, render_template, redirect, url_for, request
from application import app, db, bcrypt
from application.models import User, Pokemon
from application.forms import RegistrationForm, LoginForm, PokemonForm, UpdateAccountForm 

from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
    print(current_user)
    return render_template('home.html', title='Home')

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

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
        return redirect(url_for('home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')

            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/pokemonpage')
def pokemonpage():
    postData = Pokemon.query.all()
    return render_template('pokemonpage.html', title='Pokemon Page', posts=postData)

@app.route('/teamcreatepage', methods=['GET', 'POST'])
def teamcreatepage():
    form = PokemonForm()
    if form.validate_on_submit():
        postData = Pokemon(
                pokemon_name=form.pokemon_name.data, 
                pokemon_fast=form.pokemon_fast.data, 
                pokemon_charge=form.pokemon_charge.data
                )
        db.session.add(postData)
        db.session.commit()
        return redirect(url_for('pokemonpage'))
    return render_template('teamcreatepage.html', title='Team Create Page', form=form)

@app.route('/account', methods=['GET','POST'])
@login_required
def account():
	form = UpdateAccountForm()
	if form.validate_on_submit():
		current_user.username = formu.username.data
		current_user.email = form.email.data
		db.session.commit()
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.username.data = current_user.username
		form.email.data = current_user.email
	return render_template('account.html', title='Account', form=form)
