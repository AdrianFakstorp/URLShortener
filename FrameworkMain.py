from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Please Input Your Desired URL"

if __name__ == "__main__":
    app.run(debug=True)