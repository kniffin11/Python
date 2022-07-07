# name this file to the pluralization of the file we use, and put all routes that work with database in here

# from Python.Flask_Mysql.Db_Connection.users_cr.users_CRUD_mod.config.mysqlconnection import connectToMySQL
from flask_app import app
# import these standard files here then import this file (users_CRs.py) to server.py
from flask import render_template,redirect,request,session,flash # -- this never glows up to indicate connection
# import the class here too from flask_app.models.class_file_name
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def dojos():
    all_dojos = Dojo.get_all()
    return render_template('index.html', dojos = all_dojos)

@app.route('/new_dojo', methods = ['POST'])
def add_dojo():
    data = {"name" : request.form['dojo_name']}

    # call upon class method
    Dojo.add(data)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_one_dojo(id):
    data = {"id" : id}
    all_ninjas_in_dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template('index_one_dojo.html', all_ninjas_in_dojo = all_ninjas_in_dojo)
