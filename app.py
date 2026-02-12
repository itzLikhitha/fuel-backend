from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# -----------------------------
# TEST ROUTE (ROOT)
# -----------------------------
@app.route("/")
def home():
    return "Fuel Delivery Backend is Running Successfully!"

# -----------------------------
# USERS TABLE ROUTE
# -----------------------------
@app.route("/api/auth/users_table")
def users_table():
    data = [
        {"id": 1, "name": "Likhitha", "email": "likhi@gmail.com", "phone": "9876543210"},
        {"id": 2, "name": "Demo User", "email": "demo@gmail.com", "phone": "9999999999"}
    ]
    return jsonify(data)

# -----------------------------
# ORDERS TABLE ROUTE
# -----------------------------
@app.route("/api/fuel/orders_table")
def orders_table():
    data = [
        {"order_id": 1, "user_id": 1, "fuel_type": "Petrol", "quantity": 5, "location": "Hyderabad"}
    ]
    return jsonify(data)

# -----------------------------
# MECHANICS TABLE ROUTE
# -----------------------------
@app.route("/api/mechanics_table")
def mechanics_table():
    data = [
        {"mechanic_id": 1, "name": "Ramesh", "location": "Hyderabad"}
    ]
    return jsonify(data)

# -----------------------------
# RENDER PORT CONFIG
# -----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
