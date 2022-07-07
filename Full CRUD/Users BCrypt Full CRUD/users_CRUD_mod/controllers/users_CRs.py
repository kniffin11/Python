# name this file to the pluralization of the file we use, and put all routes that work with database in here

# import app from the __init__ file in users_CRUD_mod
from users_CRUD_mod import app
# import these standard files here then import this file (users_CRs.py) to server.py
from flask import render_template,redirect,request,session,flash # -- this never glows up to indicate connection
# import the class here too from flask_app.models.class_file_name
from users_CRUD_mod.models.users_CR import Users_CR

@app.route('/')
def read():
    print('got here')
    # call upon the get_all method to retireve the users 
    # syntax is: var_name = class_name.method_name()
    all_users = Users_CR.get_all()
    print(all_users)
    return render_template('index_read.html', users = all_users)

# to show the template
@app.route('/create')
def create():
    return render_template('index_create.html')

# to edit
@app.route('/create_post', methods=["POST"])
def create_post():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }

    # use the class method to add new data to database
    Users_CR.save(data)
    return redirect('/')

# I didn't finish the show function since i was tired, only turning in for the modularization part
@app.route('/show/<int:id>')
def show(id):
    data = {
        # only the id is needed since the link is tied to all of the data from that row
        "id": id,
    }
    user = Users_CR.get_one(data)
    return render_template('index_show.html', user = user) # can do 'user = Users_CR.get_one(data)' after 'index.html', ...

# to show the template
# the id is set on the base routes edit href within index_show.html from the for loop
@app.route('/edit_page/<int:user_id>')
def edit_page(user_id):
    return render_template('index_edit.html', id = user_id)

# to edit
# the user_id is sent from the previous route
@app.route('/edit/<int:user_id>', methods = ["POST"])
def edit(user_id):
    data = {
        "id": user_id,
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }

    Users_CR.update(data)
    return redirect('/show')

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id": id
    }
    Users_CR.delete(data)
    return redirect('/')