from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel.db'
db = SQLAlchemy(app)

class Room_Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.Integer, nullable=False)
    customer_name = db.Column(db.String(30), nullable=False)
    contact_no = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    guests = db.Column(db.Integer, nullable=False)
    check_in = db.Column(db.date, nullable=False)
    check_out = db.Column(db.date, nullable=False)
    room_type = db.Column(db.String(30), nullable=False)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/reserve',methods=['GET', 'POST'])
def room():
    if request.method == 'POST':
        customer_name = request.form[]
        check_in = request.form['check_in']
        check_out = request.form['check_out']
        guests = request.form['guests']
        

    
    
    
    
    
    
    
    
    return render_template('book_room.html')




    


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)