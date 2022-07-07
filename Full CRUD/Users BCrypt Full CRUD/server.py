from users_CRUD_mod.controllers import users_CRs # this pulls all of the routes from controllers 
from users_CRUD_mod import app # pulls the app from the init py file that is within the users_CRUD_mod folder

if __name__ == "__main__":
    app.run(debug = True)