# Python script: run with `$ fab ___command___`

# Imports from nearby files
from fabric.api import *
from setup_server import *

# Environmental Stuff
env.hosts = [
    'server.domaind.tld',  # name or ip address of server
]
env.user = 'root'    # name of user, you'll have to supply password at execution



