from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("form.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']

    try:
        age = int(age)
        if age < 0 or age > 125:
            return 'invalid age. Must be between 0 to 125.'
    except ValueError:
        return 'Age must be a number'
   
    return render_template('result.html',name=name.title(), age = age)

if __name__ == "__main__":
    app.run(debug=True)