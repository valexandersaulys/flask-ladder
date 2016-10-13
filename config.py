import os

SECRET_KEY = "beautiful_little_world_is_mine"
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# = = = = = = = For the Database Configuration
# Separate out into a 'db_config.py' for larger projects
if os.environ.get('DATABASE_URL') is None:
    DATABASE_URL = 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(BASEDIR, 'db_repository')
    SQLALCHEMY_TRACK_MODIFICATIONS = True;
else:
    DATABASE_URL = os.environ['DATABASE_URL'];  # could be mongodb

"""
Sample MongoDB Setup, if the URL is not specified as an environement variable

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
