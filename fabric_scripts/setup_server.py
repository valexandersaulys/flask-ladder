from fabric.api import *
import string,random

def update_upgrade():
    """Updates & Upgrades the server"""
    sudo("apt-get update");
    sudo("apt-get -y upgrade");


def install_nginx():
    """Install nginx"""
    sudo("apt-get install nginx");

def install_python():
    """Install python, dev, etc."""
    sudo("apt-get install python python-dev python-pip libssl-dev "\
         "libffi-dev htop munin");

def create_deploy_user():
    """creates a user for deploying a website & copy a git template over"""
    sudo("adduser deploy");
    run("git clone http://github.com/valexandersaulys/flask-ladder");
    run("virtualenv .venv");
    sudo("chown deploy:deploy .venv/");
    sudo("chown deploy:deploy flask-ladder/");
    run(".venv/bin/pip install -r flask-ladder/requirements.txt");

def install_mysql():
    """ Installs and configures MySQL for 'deploy' user """
    sudo("apt-get install mysql-server mysql-client");
    password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12));
    sudo("mysql --execute=\"CREATE USER 'deploy'@'localhost' IDENTIFIED BY '"+password+"';\"");

    # Run some mysql commands for setup
    sudo("mysql --execute=\"CREATE DATABASE deployment;\"");
    sudo("mysql --execute=\"CREATE DATABASE development;\"");
    sudo("mysql --execute=\"GRANT ALL PRIVILEGES ON deployment.* to 'deploy'@'localhost';\"");
    sudo("mysql --execute=\"GRANT ALL PRIVILEGES ON development.* to 'deploy'@'localhost';\"");

    # Then add the mysql URI to the bashrc for deploy user
    bash_insert_string = "deploy:"+password+"@localhost";  # uri for flask
    sudo("echo 'DATABASE_URI=x"+bash_insert_string+"' >> /home/deploy/.bashrc"); 

def install_mongodb():
    """ Installs and configures mongodb for 'deploy' user """
    # Install MongoDB
    sudo("apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927");
    run("echo "\
        + "'deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse'"\
        + "| sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list");
    sudo("apt-get update");
    sudo("apt-get install -y mongodb-org");

    # Unfortuantely, creating and configuring a user will not be a one liner...
    """
    db.createUser({ username:"",
    password:"", 
    roles:[ { role:"dbAdmin or readWrite",
    db: "<name_of_database>" }, ... ]
    } );
    db.getUsers(); # to get users
    show dbs  # to show users
    db.updateUser("name_of_user", { roles: [ {role: '', db: '' },... ] });
    """


def install_redis():
    """
    Installs Redis
    Run as main user
    """
    print "Installing some base dependencies"
    sudo("apt-get update");
    sudo("apt-get install -y build-essential tcl8.5");

    print "Download with wget the redis installers for ubuntu";
    run("wget http://download.redis.io/releases/redis-stable.tar.gz");
    run("tar xzf redis-stable.tar.gz");

    print "Download and run make for redis";
    run("cd redis-stable");
    run("make");
    run("make test");
    sudo("make install");

    print "Run the included script to install"
    with cd("utils"):
        sudo("./install_server.sh");
        sudo("service redis_6379 start");

    print "Run setup at startup"
    sudo("update-rc.d redis_6379 defaults");

    print "then setup security so that _only_ the localhost can access"
    sudo("echo 'bind 127.0.0.1' >> /etc/redis/6379.conf");
