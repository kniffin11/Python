from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def hello_world(): 
    return "Hello World!"

# Dojo
@app.route('/dojo')
def dojo():
    return "Dojo!"

# say
# you can specify which datatype a parameter will be by <data_type:var_name>
@app.route('/say/<name>')
def say(name):
    return f"Hello {name}!"

# repeat
@app.route('/repeat/<int:number>/<string:phrase>')
def repeat(number, phrase):
    arr_num = []
    for i in range (0, int(number)): 
        arr_num.append(phrase)
    return f"{arr_num}\n"

# -------- this is the solution ---------
    # def repeat_word(num, word):
    # output = ''

    # for i in range(0,num):
    #     output += f"<p>{word}</p>"

    # return output
# ---------------------------------------

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    # app.run(debug=True) should be the very last statement! 
    app.run(debug=True)    # Run the app in debug mode.