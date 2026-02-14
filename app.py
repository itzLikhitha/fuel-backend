from flask import Flask
from flask_cors import CORS
import os

# Import Blueprints
from routes.auth_routes import auth_bp
from routes.fuel_routes import fuel_bp
from routes.mechanic_routes import mechanic_bp

app = Flask(__name__)
CORS(app)

# -----------------------------
# REGISTER BLUEPRINTS WITH PREFIX
# -----------------------------
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(fuel_bp, url_prefix="/api/fuel")
app.register_blueprint(mechanic_bp, url_prefix="/api")

# -----------------------------
# HOME ROUTE
# -----------------------------
@app.route("/")
def home():
    return "Fuel Delivery Backend Running Successfully!"

# -----------------------------
# RENDER PORT CONFIG
# -----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
