from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    # request.form is used when the origninal route was a post method and had a form; then you can call upon each key as the request.form makes a tuple
    print(request.form)
    first_name = request.form['first_name'] 
    last_name = request.form['last_name'] 
    student_id = request.form['student_id'] 
    strawberry = request.form['strawberry'] 
    raspberry = request.form['raspberry'] 
    apple = request.form['apple'] 
    blackberry = request.form['blackberry'] 
    total = int(strawberry) + int(raspberry) + int(apple) + int(blackberry)
    return render_template("checkout.html", fn = first_name, ln = last_name, s_id = student_id, straw = int(strawberry), rasp = int(raspberry), ap = int(apple), bl = int(blackberry), total = total)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    