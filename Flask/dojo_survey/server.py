from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "tsuyinjom93"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summary():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['favorite_langauge'] = request.form['favorite_langauge']
    session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html', name = session['name'], loc = session['location'], fav_lang = session['favorite_langauge'], com = session['comments'])

if (__name__ == "__main__"):
    app.run(debug = True)