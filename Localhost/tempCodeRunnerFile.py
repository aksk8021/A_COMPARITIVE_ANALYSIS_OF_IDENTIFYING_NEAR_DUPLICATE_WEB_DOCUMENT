from flask import Flask
from flask import render_template,request,redirect
app = Flask(__name__)

@app.route("/")
def root():
    return render_template("root.html")