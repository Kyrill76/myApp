import sys
import os


##Virtualenv Settings
activate_this = '/var/www/myApp/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

##Replace the standard out
sys.stdout = sys.stderr

##Add this file path to sys.path in order to import app
sys.path.append('/var/www/myApp/')

from myApp import app as application
