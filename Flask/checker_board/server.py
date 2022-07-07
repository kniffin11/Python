from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def eight_by_eight():
    return render_template('index.html', x = 8, y = 8, color1 = 'red', color2 = 'black')

@app.route('/<int:x>')
def x_by_eight(x):
    return render_template('index.html', x = x, y = 8, color1 = 'red', color2 = 'black')

@app.route('/<int:x>/<int:y>')
def x_by_y(x,y):
    return render_template('index.html', x = x, y = y, color1 = 'red', color2 = 'black')

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def x_by_y_colors(x,y, color1, color2):
    return render_template('index.html', x = x, y = y, color1 = color1, color2 = color2)

if __name__=="__main__":
    app.run(debug=True)
