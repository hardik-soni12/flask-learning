from flask import Flask, flash, redirect, url_for, render_template, request
from forms import registrationForm

app = Flask(__name__)
app.secret_key ='my-secret-key'

@app.route('/', methods=["GET", "POST"])
def register():
    form = registrationForm()
    if request.method == "POST":
        if form.validate_on_submit():
            name = form.name.data
            email = form.email.data
            # password = form.password.data
            flash(f"Welcome, {name}!! you registered successfully!","success")
            return redirect(url_for('success'))
        else: 
            flash("something went wrong!","danger")
            return render_template("register.html", form = form)
        
    return render_template('register.html', form = form)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True, port=5005) 