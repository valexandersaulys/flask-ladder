import os, datetime
from app import app, db, logger
from flask import render_template, flash, redirect, session, url_for, \
    request, g, send_from_directory

# - - - - - - - Custom Routing
@app.errorhandler(404)
def error_404():
    # Haven't actually tried this yet
    return render_template("404.html")
    
# - - - - - - - Main Routes
@app.route("/")
@app.route("/index",methods=['GET'])
def main_page():
    # Display main login page
    return render_template("index.html")
