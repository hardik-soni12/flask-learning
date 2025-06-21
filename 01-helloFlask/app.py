from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p><i>Hello, Flask!!<br>Welcome to Day 1.</i></p>"

if __name__ == "__main__":
    app.run(debug=True)