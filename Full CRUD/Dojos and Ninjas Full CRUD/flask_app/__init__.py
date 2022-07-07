# this always goes in templates and gets imported as: from flask_app import app 

from flask import Flask
app = Flask(__name__)
app.secret_key = "aw34tg"