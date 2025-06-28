from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/users")
def users():
    users_list = ['Hardik','Aniket','Sanskar','Abhishek','Swapnil']
    return render_template("users.html",users = users_list)

if __name__ == '__main__':
    app.run(debug=True)