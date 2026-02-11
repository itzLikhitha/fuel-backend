from database.db import db

class Mechanic(db.Model):
    __tablename__ = 'mechanics'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    is_available = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"<Mechanic {self.name}>"
