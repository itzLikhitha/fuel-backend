from flask import Blueprint
from models import db, FuelOrder

fuel_bp = Blueprint('fuel', __name__, url_prefix='/api/fuel')

@fuel_bp.route('/add_order/<int:user_id>/<fuel>/<int:qty>/<address>')
def add_order(user_id, fuel, qty, address):
    order = FuelOrder(
        user_id=user_id,
        fuel_type=fuel,
        quantity=qty,
        address=address
    )
    db.session.add(order)
    db.session.commit()
    return "Order placed successfully"

@fuel_bp.route('/orders_table')
def orders_table():
    orders = FuelOrder.query.all()
    html = "<h2>Fuel Orders</h2><table border=1><tr><th>ID</th><th>User ID</th><th>Fuel</th><th>Qty</th><th>Address</th></tr>"
    for o in orders:
        html += f"<tr><td>{o.id}</td><td>{o.user_id}</td><td>{o.fuel_type}</td><td>{o.quantity}</td><td>{o.address}</td></tr>"
    html += "</table>"
    return html
