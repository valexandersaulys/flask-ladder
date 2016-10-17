#!/bin/bash

# Bash script to download the different javascript and css files
# Updated as of 10 - 17 - 2016

# Minified & Zipped Downloads
wget https://code.jquery.com/jquery-3.1.1.min.js
wget http://backbonejs.org/backbone-min.js
wget https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css
wget https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css #optional
wget https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js #optional
wget http://underscorejs.org/underscore-min.js

# Also, the non-min versions for development (if useful)
#wget https://code.jquery.com/jquery-3.1.1.js
#wget http://backbonejs.org/backbone.js
#wget https://github.com/twbs/bootstrap/releases/download/v3.3.7/bootstrap-3.3.7-dist.zip
#wget http://underscorejs.org/underscore.js