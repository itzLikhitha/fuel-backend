from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# ---------------- USER ----------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(15))

# ---------------- FUEL ORDER ----------------
class FuelOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    fuel_type = db.Column(db.String(50))
    quantity = db.Column(db.Integer)
    address = db.Column(db.String(200))

# ---------------- MECHANIC ----------------
class Mechanic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.String(15))
    location = db.Column(db.String(100))
