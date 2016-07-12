from app import db
from passlib.apps import custom_app_context as pwd_context
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    # All models should have an 'id' 
    id = db.Column(db.Integer, index=True, primary_key=True)
    
    # Standard user stuff
    username = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128), unique=True)  

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        # what gets printed in the console during debugging
        return "<User %r>" % (self.username)
