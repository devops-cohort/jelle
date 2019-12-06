from application import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return ''.join(['User ID: ', str(self.id), '\r\n', 'Email: ', self.email])

class Pokemon(db.Model):
    pokemon_name = db.Column(db.String(30), nullable=False, unique=True, primary_key=True)
    pokemon_fast = db.Column(db.String(30), nullable=False, unique=False)
    pokemon_charge = db.Column(db.String(30), nullable=False, unique=True)

    def __repr__(self):
        return ''.join(['Name: ', str(self.pokemon_name), '\r\n', 'Move: ', str(self.pokemon_fast), '\r\n', 'Email: ', str(self.pokemon_charge)])
