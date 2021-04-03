from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

#sqlAlchemy is an orm for flask here using sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db' #creating database todo.db at root folder
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) #creating db which has database

class Todo(db.Model):  # class to create database schema it must have a primary key
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:  #repr function to print in python shell
        return f"{self.title}"
 #to create database open python shell and execute  from app import db then db.create_all()

#home route
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        new_title = request.form['title']
        new_desc = request.form['desc']
        todo = Todo(title=new_title, desc=new_desc)
        db.session.add(todo)
        db.session.commit()
        return redirect("/")

    alltodo = Todo.query.all()
    return render_template('index.html',alltodo = alltodo) 


@app.route('/delete/<int:sno>')
def delete(sno):
    todel = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todel)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method == 'POST':
        toupdatetodo = Todo.query.filter_by(sno=sno).first()
        up_title = request.form['title']
        up_desc = request.form['desc']
        
        toupdatetodo.title = up_title
        toupdatetodo.desc = up_desc

        db.session.add(toupdatetodo)
        db.session.commit()

        return redirect('/')

#main method
if __name__ == "__main__":
    app.run(debug=True)
