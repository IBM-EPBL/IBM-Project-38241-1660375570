from flask import Flask, url_for, render_template
from markupsafe import escape

app = Flask(__name__)




@app.route("/index1")
def index1():
    return render_template('index1.html')

@app.route("/profile")
def profile():
     return render_template('profile.html')

@app.route("/signup1")
def signup1():
     return render_template('signup1.html')
