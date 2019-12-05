from application import db, login_manager

class Users(db.model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    
    def __repr__(self):
        return ''.join(['User ID: ', str(self.id), '\r\n', 'Email: ', self.email])
