from flask import Flask, render_template, request, redirect
from flask_cors import CORS
from models import db
from routes.auth_routes import auth_bp
from routes.fuel_routes import fuel_bp
from routes.mechanic_routes import mechanic_bp

app = Flask(__name__)
CORS(app)


# ---------------- CONFIG ----------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fuel_delivery.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# ---------------- BLUEPRINTS ----------------
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(fuel_bp, url_prefix="/api/fuel")
app.register_blueprint(mechanic_bp, url_prefix="/api/mechanics")

# ---------------- CREATE TABLES ----------------
with app.app_context():
    db.create_all()

# ---------------- HOME PAGE ----------------
@app.route('/')
def home():
    return render_template('index.html')

# ---------------- ADD USER FORM ----------------
@app.route('/add_user', methods=['GET', 'POST'])
def add_user_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        return redirect(f"/api/auth/add_user/{name}/{email}/{phone}")

    return '''
        <h2>Add User</h2>
        <form method="post">
            Name: <input name="name"><br><br>
            Email: <input name="email"><br><br>
            Phone: <input name="phone"><br><br>
            <button type="submit">Add User</button>
        </form>
        <br>
        <a href="/">Back to Home</a>
    '''

# ---------------- ADD FUEL ORDER FORM ----------------
@app.route('/add_order', methods=['GET', 'POST'])
def add_order_form():
    if request.method == 'POST':
        user_id = request.form['user_id']
        fuel_type = request.form['fuel_type']
        quantity = request.form['quantity']
        address = request.form['address']
        return redirect(
            f"/api/fuel/add_order/{user_id}/{fuel_type}/{quantity}/{address}"
        )

    return '''
        <h2>Add Fuel Order</h2>
        <form method="post">
            User ID: <input name="user_id"><br><br>
            Fuel Type: <input name="fuel_type"><br><br>
            Quantity: <input name="quantity"><br><br>
            Address: <input name="address"><br><br>
            <button type="submit">Place Order</button>
        </form>
        <br>
        <a href="/">Back to Home</a>
    '''

# ---------------- ADD MECHANIC FORM ----------------
@app.route('/add_mechanic', methods=['GET', 'POST'])
def add_mechanic_form():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        location = request.form['location']
        return redirect(
            f"/api/mechanics/add/{name}/{phone}/{location}"
        )

    return '''
        <h2>Add Mechanic</h2>
        <form method="post">
            Name: <input name="name"><br><br>
            Phone: <input name="phone"><br><br>
            Location: <input name="location"><br><br>
            <button type="submit">Add Mechanic</button>
        </form>
        <br>
        <a href="/">Back to Home</a>
    '''

# ---------------- RUN SERVER ----------------
@app.route('/users_table')
def users_table():
    users = db.session.execute("SELECT * FROM user").fetchall()
    table_html = "<h2>Users Table</h2><table border='1'><tr><th>ID</th><th>Name</th><th>Email</th><th>Phone</th></tr>"
    for u in users:
        table_html += f"<tr><td>{u.id}</td><td>{u.name}</td><td>{u.email}</td><td>{u.phone}</td></tr>"
    table_html += "</table><br><a href='/'>Back to Home</a>"
    return table_html
@app.route('/orders_table')
def orders_table():
    orders = db.session.execute("SELECT * FROM fuel_order").fetchall()
    table_html = "<h2>Fuel Orders Table</h2><table border='1'><tr><th>ID</th><th>User ID</th><th>Fuel Type</th><th>Quantity</th><th>Address</th></tr>"
    for o in orders:
        table_html += f"<tr><td>{o.id}</td><td>{o.user_id}</td><td>{o.fuel_type}</td><td>{o.quantity}</td><td>{o.address}</td></tr>"
    table_html += "</table><br><a href='/'>Back to Home</a>"
    return table_html
@app.route('/mechanics_table')
def mechanics_table():
    mechanics = db.session.execute("SELECT * FROM mechanic").fetchall()
    table_html = "<h2>Mechanics Table</h2><table border='1'><tr><th>ID</th><th>Name</th><th>Phone</th><th>Location</th></tr>"
    for m in mechanics:
        table_html += f"<tr><td>{m.id}</td><td>{m.name}</td><td>{m.phone}</td><td>{m.location}</td></tr>"
    table_html += "</table><br><a href='/'>Back to Home</a>"
    return table_html

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)