WTF_CSRF_ENABLED = True
SECRET_KEY = "beautiful_little_world_is_mine"

import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# = = = = = = = For the Database Configuration
if os.environ.get('DATABASE_URL') is None:
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'];

SQLALCHEMY_MIGRATE_REPO = os.path.join(BASEDIR, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True;

"""
Sample MongoDB Setup is below:
MONGODB_DB = 'project1'
MONGODB_HOST = '192.168.1.35'
MONGODB_PORT = 12345
MONGODB_USERNAME = 'webapp'
MONGODB_PASSWORD = 'pwd123'
"""

# - - - - - - - Put Constants here
"""
Examples can include bits like constants for folder storage
"""
