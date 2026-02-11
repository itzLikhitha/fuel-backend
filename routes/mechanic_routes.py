from flask import Blueprint
from models import db, Mechanic

mechanic_bp = Blueprint('mechanics', __name__, url_prefix='/api/mechanics')

@mechanic_bp.route('/add/<name>/<phone>/<location>')
def add_mechanic(name, phone, location):
    mech = Mechanic(name=name, phone=phone, location=location)
    db.session.add(mech)
    db.session.commit()
    return "Mechanic added"

@mechanic_bp.route('/mechanics_table')
def mechanics_table():
    mechs = Mechanic.query.all()
    html = "<h2>Mechanics</h2><table border=1><tr><th>ID</th><th>Name</th><th>Phone</th><th>Location</th></tr>"
    for m in mechs:
        html += f"<tr><td>{m.id}</td><td>{m.name}</td><td>{m.phone}</td><td>{m.location}</td></tr>"
    html += "</table>"
    return html
