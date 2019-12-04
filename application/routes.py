from flask import Flask, render_template
from application import app

@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/pokemonpage')
def pokemonpage():
    return render_template('pokemonpage.html', title='Pokemon Page')

@app.route('/fastmovespage')
def fastmovespage():
    return render_template('fastmovespage.html', title='Fast Moves Page')

@app.route('/chargemovespage')
def chargemovespage():
    return render_template('chargemovespage.html', title='Charge Moves Page')
