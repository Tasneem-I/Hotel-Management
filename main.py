import random
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
#Initiating flask
app = Flask(__name__)

#Confiquring SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel.db'
db = SQLAlchemy(app)

#Defining a table called room and storing the room numbers
class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer())

class Room_Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.Integer, nullable=False)
    customer_name = db.Column(db.String(30), nullable=False)
    contact_no = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    guests = db.Column(db.Integer, nullable=False)
    check_in = db.Column(db.Date, nullable=False)
    check_out = db.Column(db.Date, nullable=False)
    room_type = db.Column(db.String(30), nullable=False)

with app.app_context():
    db.create_all()
with app.app_context():
   room_data=[{'number': 101},{'number': 102},{'number': 103},{'number': 104},
       {'number': 105},{'number': 106},{'number': 107},{'number': 108},
       {'number': 109},{'number': 110},{'number': 111},{'number': 112},
       {'number': 113},{'number': 114},{'number': 115},{'number': 116},
       {'number': 117},{'number': 118},{'number': 119},{'number': 120}]
   for r in room_data:
        new_room = Room(**r)
        db.session.add(new_room)
        db.session.commit()

#Defining table for booking room


#defining page routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/reserve',methods=['GET', 'POST'])

def book():
    if request.method == 'POST':
        room_number = find_available_room_number()
        customer_name = request.form['customer_name']
        contact_no = request.form['contact_no']
        email = request.form['email']
        check_in = request.form['check_in']
        check_out = request.form['check_out']
        guests = request.form['guests']
        room_type = request.form['room_type']
        booking = Room_Booking(room_number=room_number,customer_name=customer_name,contact_no=contact_no,
                          email=email,check_in=check_in,check_out=check_out,guests=guests,room_type=room_type)
        db.session.add(booking)
        db.session.commit()
        return 
    return render_template('book_room.html')
def find_available_room_number():
    used_room_numbers = [b.room_number for b in Room_Booking.query.all()]
    available_room_numbers = [r.number for r in Room.query.all() if r.number not in used_room_numbers]
    return random.choice(available_room_numbers)

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)