from flask import Flask, request, Response, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "supersecret"

#homepage Login page
@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "riooo@23" and password == "222325":
            session["user"] = username #store in seesion
            return redirect(url_for("welcome"))
        else:
            return Response("In-valid Credentials, Try again", mimetype="text/plain")
    
    return '''
            <h2>Login Page</h2>
            <form method="POST">
            username: <input type="text" name="username" required><br><br>
            password: <input type="password" name="password" required><br><br>
            <input type="submit" value="login">
            </form>

            '''

# Welcome Page(after loogin)
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
            <h2>Welcome, {session["user"]}!</h2>
            <a href={url_for('logout')}>logout</a>
        '''
    return redirect(url_for("login"))

#logout route
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)