from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secret key"

@app.route('/')
def index():
    return render_template('index.html')

# /users because the action attirbute of the HTML form is 'users'- and when  you press submit, it submits 'users'.
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # the data that comes through with request.form will be a string no matter what 
    print(request.form)

    # since we are using a session, we can remember variables accross functions (each route is by default, independent from any other route; ignorant)
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']

    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    return redirect('/') # the example said to change 

# never render a template on a post route
@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])

if(__name__ == "__main__"):
    app.run(debug = True)