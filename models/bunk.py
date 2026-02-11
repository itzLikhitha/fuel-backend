from database.db import db

class Bunk(db.Model):
    __tablename__ = 'bunks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    fuel_types = db.Column(db.String(100), nullable=False)  # e.g., Petrol, Diesel
    phone = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return f"<Bunk {self.name}>"
