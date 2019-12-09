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

#Rout to login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    #If already logged in, redirect to home page
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    #Creates the form to log in-in forms.py
    form = LoginForm()
    #If form is valid
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        #If password relates to email
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')

            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

#Route to log out a currently logged in user
@app.route('/logout')
def logout():
    logout_user()
    #Once logged out, send user to login page
    return redirect(url_for('login'))

#Route to page with caught pokemon
@app.route('/pokemonpage')
def pokemonpage():
    #Queries information from the Pokemon table
    postData = Pokemon.query.all()
    return render_template('pokemonpage.html', title='Pokemon Page', posts=postData)

#Route to the team creation page
@app.route('/teamcreatepage', methods=['GET', 'POST'])
def teamcreatepage():
    user_id = current_user
    #Sets up the form
    form = PokemonForm()
    if form.validate_on_submit():
        #Data needed to be enetered in the form
        postData = Pokemon(
                pokemon_name=form.pokemon_name.data, 
                pokemon_fast=form.pokemon_fast.data, 
                pokemon_charge=form.pokemon_charge.data,
                user_id = current_user.id
                )
        #Adds and commits the inputted data to the table
        db.session.add(postData)
        db.session.commit()
        return redirect(url_for('pokemonpage'))
    return render_template('teamcreatepage.html', title='Team Create Page', form=form)

#Route to the account page
@app.route('/account', methods=['GET','POST'])
#User must be logged in to access it
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

#Route to delete the account
@app.route('/deleteaccount', methods=['GET', 'POST'])
#Must be logged in to access it
@login_required
def deleteaccount():
    user = current_user.id
    account = current_user
    db.session.delete(account)
    db.session.commit()
    return redirect(url_for('home'))

#Route to log out a currently logged in user
@app.route("/index")
def index():
    return render_template('index.html', title='Coverage')
