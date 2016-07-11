#!.venv/bin/python
"""
First version of my custom scripting file
"""
# - - - - - - - - Header Crap
from app import db, app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)
DATABASE_TYPE = "sqlite"

# - - - - - - Skeleton layout files
def build_init(dr):
    name_of_file = os.path.join(dr,"__init__.py")
    f = open(name_of_file,"w+")
    f.write("from flask import Flask\n")
    f.write("flask.ext.sqlalchemy import SQLAlchemy\n")
    f.write("import os, time\n")
    f.write("from config import BASEDIR\n")
    f.write("\n")
    f.write("app = Flask(__name__)\n")
    f.write("app.config.from_object('config')\n")
    f.write("db = SQLAlchemy(app)\n")
    f.write("\n\n\n  # - - - - Logging\b")
    f.write("import logging\n")
    f.write("from logging.handlers import RotatingFileHandler\n")
    f.write("file_handler = RotatingFileHandler('activities.log',maxBytes=100000,backupCount=2)\n")
    f.write("file_handler.setLevel(10)\n")
    f.write("app.logger.addHandler(file_handler)\n")
    f.write("app.logger.setLevel(level=0)\n")
    f.write("logger = app.logger\n")
    f.write("\n\n\n # =================== \n")
    f.write("from app import views, models\n")
    f.close()
    return 0

def build_views(dr):
    name_of_file = os.path.join(dr,"views.py")
    f = open(name_of_file,"w+")
    f.write("from app import app, db, logger\n")
    f.write("from flask import render_template, redirect, session, url_for, " + \
            "request, g, send_from_directory\n")
    f.write("from app import models\n")  # might be 'import app.models'
    f.close()
    return 0

def build_base_models(dr):
    name_of_file = os.path.join(dr,"models.py")
    f = open(name_of_file,"w+")
    f.write("from app import db\n")
    f.write("from wekzeug.security import generate_password_hash, check_password_hash\n")
    f.close()
    return 0

def build_utils(dr):
    name_of_file = os.path.join(dr,"utils.py")
    f = open(name_of_file,"w+")
    f.close()
    return 0

def build_static_folder(dr):
    os.mkdir(os.path.join(dr,"static"))
    name_of_file = os.path.join(dr,"static","styles.css")
    f = open(name_of_file,"w+")
    f.close()
    return 0

def build_templates_folder(dr):
    os.mkdir(os.path.join(dr,"templates"))
    return 0    

def build_404(dr):
    name_of_file = os.path.join(dr,"templates","404.html")
    f = open(name_of_file,"w+")
    f.write("<h1>ERR0R: 404, Not Found</h1>")
    f.close()
    return 0

def build_base_view(dr):
    name_of_file = os.path.join(dr,"templates","base.html")
    f = open(name_of_file,"w+")
    f.write("<!doctype html>\n")
    f.write("<html>\n")
    f.write("  <head>\n")
    f.write("    {% block head %}\n")
    f.write("    {% endblock %}\n")
    f.write("  </head>\n")
    f.write("  <body>\n")
    f.write("    {% block content %}\n")
    f.write("    {% endblock %}\n")    
    f.write("  </body>\n")
    f.write('  <script type="text/javascript">\n')
    f.write("    {% block jquery_script %}\n")
    f.write("    {% endblock %}\n")
    f.write('  </script>\n')
    f.write("</html>\n")
    f.close()
    return 0

def build_index(dr):
    name_of_file = os.path.join(dr,"templates","index.html")
    f = open(name_of_file,"w+")
    f.write("{% extends 'base.html' %}\n")
    f.write("{% block content %}\n")
    f.write("<h1>This is the homepage!</h1>\n")
    f.write("{% endblock %}\n")
    f.close()
    return 0

def copy_manage(dr):
    # TO-DO: How to copy this file over, default install somewhere?
    pass

def build_config(dr):
    name_of_file = os.path.join(dr,"..","config.py") # go back one directory
    f = open(name_of_file,"w+")
    f.write("import os\n")
    f.write("BASEDIR = os.path.abspath(os.path.dirname(__file__))\n")

    # TO-DO: How to build constants for the database, dependent on type of database
    return 0

def build_run(dr):
    name_of_file = os.path.join(dr,"run.py")
    f = open(name_of_file,"w+")
    f.write("#!.venv/bin/python\n")
    f.write("from app import app\n")
    f.write("app.run(host='0.0.0.0')\n")
    f.close()
    return 0

def build_wsgi(dr):
    name_of_file = os.path.join(dr,"wsgi.py")
    f = open(name_of_file,"w+")
    f.write("from app import app\n\n")
    f.write("if __name__ == '__name__':\n")
    f.write("    app.run(host='0.0.0.0');\n");
    f.close()
    return 0


# - - - - - - - - - - - - - - - - - - - - -
def call_model(name,params):
    """
    To-Do:
      * builds a model based on DATABASE_TYPE into 'models.py'
      * parses syntax from params (should be straight string)
    """

    # parsing example
    fields = params.split(' ');
    for field in fields:
        a = field.split(":")
        # a[0] will be the field name
        # a[1] will be the type of entry to create
    pass

def call_blueprint(name,params):
    # REUSABILITY: ability to call_blueprint with name 'app' for creating a new app
    """
    To-Do:
      * pretty much recreates the new project, but the app aspect
    """
    pass


# - - - - - - - - - - Big Command Functions
@manager.option('-n','--name',dest='name',default='default')
@manager.option('-d','--database',dest='database',default=None)
def startproject(name, database):
    """
    To-Do:
      * builds directory 'name', and 'name/app'
      * builds config, manage, run, wsgi in 'name' directory
      * builds forms, models, utils, views, static, templates, 404, base, index into 'app' dir
    """
    pass

@manager.option('-t','--type',dest='call',default=None)
@manager.option('-n','--name',dest='name',default=None)
@manager.option('-e','--extra-options',dest='params',default=None)
def build(call,name,params):
    if call=="model":
        call_model(name,params);
    elif call=="blueprint":
        call_blueprint(name,params);
    else:
        print("unknown build %s called" % call);


if __name_=="__main__":
    manager.run()
