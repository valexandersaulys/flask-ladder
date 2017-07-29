from . import app
from .utils import hash_generator

@app.before_request
def csrf_protect():
    if request.method == "POST":
        token = session.pop("_csrf_token", None);
        if not token or token != request.form.get("_csrf_token"):
            abort(403);

def generate_csrf_token():
    if "_csrf_token" not in session:
        session["_csrf_token"] = hash_generator(30);
    return session["_csrf_token"];

app.jinja_env.globals['csrf_token'] = generate_csrf_token
