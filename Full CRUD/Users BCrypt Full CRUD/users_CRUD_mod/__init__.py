# this always goes in templates and gets imported as: from user_CRUD_mod import app 

from flask import Flask
app = Flask(__name__)
app.secret_key = "whufoen"