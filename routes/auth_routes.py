from flask import Blueprint
from models import db, User

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/add_user/<name>/<email>/<phone>')
def add_user(name, email, phone):
    existing = User.query.filter_by(email=email).first()
    if existing:
        return "User already exists"

    user = User(name=name, email=email, phone=phone)
    db.session.add(user)
    db.session.commit()
    return "User added successfully"

@auth_bp.route('/users_table')
def users_table():
    users = User.query.all()
    html = "<h2>Users</h2><table border=1><tr><th>ID</th><th>Name</th><th>Email</th><th>Phone</th></tr>"
    for u in users:
        html += f"<tr><td>{u.id}</td><td>{u.name}</td><td>{u.email}</td><td>{u.phone}</td></tr>"
    html += "</table>"
    return html
