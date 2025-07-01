from flask import Flask, flash, redirect, url_for, render_template, request

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        users = {
            "riooo": "222325", "admin":"123", "hardik9156":"r0ck5t@r"
        }

        if username in users and password == users[username]:
            flash("Login Successful!!", "success")
            return render_template("dashboard.html", name = username.title())
        else:
            flash("invalid Username or Password", "danger")
            return redirect(url_for("login"))
        
    return render_template("login.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

if __name__ == '__main__':
    app.run(debug=True, port=5003)