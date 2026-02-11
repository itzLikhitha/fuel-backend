from database.db import db
from models.user import User

class FuelOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # <-- FIX
    fuel_type = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), default='Pending')

    # Optional: define relationship (not required for simple queries)
    user = db.relationship('User', backref=db.backref('orders', lazy=True))
