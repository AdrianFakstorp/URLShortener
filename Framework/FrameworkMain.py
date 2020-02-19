from flask import Flask, render_template, request

app = Flask(__name__)

# app.config['SECRET_KEY'] = "fb07659371ef163e955598bea0fecf44"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/text-input")
def forms():
    return render_template('forms.html')

@app.route("/text-input", methods=['POST'])
def forms_post():
    text = request.form['Input Your URL Here']
    return text
    
if __name__ == "__main__":
    app.run(debug=True)