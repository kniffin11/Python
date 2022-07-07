# name this file to the pluralization of the file we use, and put all routes that work with database in here

# import app from the __init__ file in users_CRUD_mod
from flask_app import app
# import these standard files here then import this file (users_CRs.py) to server.py
from flask import render_template,redirect,request,session,flash # -- this never glows up to indicate connection
# import the class here too from flask_app.models.class_file_name
from flask_app.models.ninja import Ninja
# importing this for the drop down menu in add ninja
from flask_app.models.dojo import Dojo


@app.route('/ninjas')
def ninjas():
    print('got here')
    all_dojos = Dojo.get_all()
    return render_template('index_add_ninja.html', dojos = all_dojos)

@app.route('/ninjas_add', methods = ['POST'])
def ninjas_add():
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age'],
        "dojo_id" : request.form['dojo_id']
    }
    
    Ninja.new_ninja(data)
    return redirect('/dojos')