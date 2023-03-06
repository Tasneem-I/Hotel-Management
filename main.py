from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel.db'
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/')
def room():
    return render_template('book_room.html')
class Room_Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.Integer, nullable=False)
    


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)