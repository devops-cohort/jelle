from flask import Flask, render_template
from application import app, db, bcrypt
from application.models import User
from application.forms import RegistrationForm

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
        return redirect(url_for('post'))
    return render_template('register.html', title='Register', form=form)

@app.route('/pokemonpage')
def pokemonpage():
    return render_template('pokemonpage.html', title='Pokemon Page')

@app.route('/fastmovespage')
def fastmovespage():
    return render_template('fastmovespage.html', title='Fast Moves Page')

@app.route('/chargemovespage')
def chargemovespage():
    return render_template('chargemovespage.html', title='Charge Moves Page')
