from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Home Page!"

@app.route("/about")
def about():
    return "This is the About Page!"

@app.route("/contact")
def contact():
    return "Contact us at imailhr1k@gmail.com"

@app.route("/user/<username>")
def greet_user(username):
    return f"Hello, {username.title()}!"

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"This is Post #{post_id}"

if __name__ == "__main__":
    app.run(debug=True)