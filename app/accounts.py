# 'User' Model (for MySQL)
from app import app, db
from werkzeug.security import generate_password_hash, \
    check_password_hash

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


# login_required decorator
from functools import wraps
from flask import g, request, redirect, url_for

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g["user"] is None:
            return redirect( url_for("login_page") );
        return f(*args, **kwargs)
    return decorated_function


# login pages
@app.route("/login_page",methods=["GET"])
def login_page():
    return render_template("login_page.html")

@app.route("/login",methods=["POST"])
def login():

    if request.headers['Content-Type'] == "application/json":
        name_of_user = request.json['username']
        pass_check = request.json['password']
        """
        Store & then return some random hash as a key for
        authentication. Then check for it as a login in a 
        RESTful authentication.

        from flask import jsonify
        from app import authhashes
        from app.utils import hash_generator
        
        hashname = hash_generator();
        authhashes[hashname] = name_of_user;
        return jsonify(authkey=hashname);
        """
    else:
        name_of_user = request.form["username"]
        pass_check = request.form["password"]
    
    u = db.session.query(User).\
        filter_by(username=request.form['username']).first()
    if u is not None:
        verification = u.check_password(pass_check)
        if verification==True:
            g["user"] = u.username;
            logger.info("User %s Has Logged in" % str(session['user']))
            return redirect( url_for("homepage") );
    return render_template("error.html");

@app.route("/logout",methods=['GET','POST'])
def logout():
    g["user"] = None;
    logger.info("User %s Has Logged Out" % str(session['user']));
    return redirect( url_for("homepage") )
