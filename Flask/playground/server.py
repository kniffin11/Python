# do pipenv install flask in cmd  
from flask import Flask, render_template  
app = Flask(__name__)

@app.route('/play')
def hellos():
    return render_template('index.html', num = 3)

@app.route('/play/<int:num>')
def hi(num):
    return render_template('index.html', num = num)

@app.route('/play/<int:num>/<string:color>')
def hey(color, num):
    return render_template('index.html', num = num,  color = color)

if __name__=="__main__":
    app.run(debug=True)