#imports
from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy

#my App
app=Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

if __name__ in "__main__":
    app.run(debug=True)