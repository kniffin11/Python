from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "fytguumi"

# render the template 
@app.route('/')
def index():
    # doubles as initializer, dont need an if to check if in session
    session['total'] += 1
    return render_template('index.html', num = session['total'])

# this is the form, redirect
@app.route('/count', methods=["POST"])
def counter():
    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def destroy():
    if 'total' in session:
        session['total'] = 0
    return redirect('/')

@app.route('/plus_2', methods=['POST'])
def plus_two():
    if 'total' in session:
        # only one because the redirect adds one too
        session['total'] += 1
    return redirect('/')

@app.route('/plus_any', methods=['POST'])
def plus_any():
    if 'total' in session:
        num = request.form['my_num']
        # -1 because the redirect adds one 
        session['total'] += (int(num) - 1)
    return redirect('/')

if (__name__ == "__main__"):
    app.run(debug = True)