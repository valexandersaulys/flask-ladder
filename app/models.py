from app import db
from werkzeug.security import generate_password_hash, \
    check_password_hash

class SimpleModel(db.Model):
    id = db.Column(db.Integer, index=True, primary_key=True)

    def __repr__(self):
        return "<ID #%r>" % (self.id);


