from application import db, login_manager
from flask_login import UserMixin
from sqlalchemy.orm import relationship

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


"""substable = db.Table('subs',
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.pokemon_id'))
        )"""

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    pokemon = db.relationship('Pokemon', backref='user', lazy=True)
    
    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.username)
            ])

class Pokemon(db.Model):
    pokemonid = db.Column(db.Integer, primary_key=True)
    pokemon_name = db.Column(db.String(30), nullable=False, unique=True)
    pokemon_fast = db.Column(db.String(30), nullable=False, unique=False)
    pokemon_charge = db.Column(db.String(30), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    

    def __repr__(self):
        return ''.join([
            'Pokemon Name: ', str(self.pokemon_name), '\r\n',
            'Fast Move: ', str(self.pokemon_fast), '\r\n',
            'Charge Move: ', str(self.pokemon_charge)
            ])
