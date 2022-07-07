from flask_app.controllers import dojos, ninjas # this pulls all of the routes from controllers: Dojo and Ninja 
from flask_app import app # pulls the app from the init py file that is within the flask_app folder

if __name__ == "__main__":
    app.run(debug = True)