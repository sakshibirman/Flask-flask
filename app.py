#imports
from flask import Flask, render_template, redirect, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

#my App
app=Flask(__name__)
Scss(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db= SQLAlchemy(app)

ist = pytz.timezone('Asia/Kolkata')

class MyTask(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    content =db.Column(db.String(100), nullable=False)
    complete =db.Column(db.Integer, default=0)
    created=db.Column(db.DateTime, default=lambda: datetime.datetime.now(ist))

    def __repr__(self) -> str:
        return f"Task {self.id}"

#home page
@app.route("/", methods=["POST","GET"])
def index():
    #Add a task
    if request=="POST":
        current_task=request.form['content']
        new_task=MyTask(content=current_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(f"ERROR:{e}")
            return f"ERROR:{e}"    
    #See Current Task
    else:
        tasks = MyTask.query.order_by(MyTask.created).all()

        return render_template("index.html", tasks=tasks)










if __name__ in "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)