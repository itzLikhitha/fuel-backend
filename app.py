from flask import Flask
from flask_cors import CORS
from database.db import db

# Import Blueprints
from routes.auth_routes import auth_bp
from routes.fuel_routes import fuel_bp
from routes.mechanic_routes import mechanic_bp

app = Flask(__name__)

# Enable CORS
CORS(app)

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fuel_delivery.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize Database
db.init_app(app)

with app.app_context():
    db.create_all()

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(fuel_bp)
app.register_blueprint(mechanic_bp)


# Home Route
@app.route("/")
def home():
    return "Fuel Delivery Backend Running Successfully 🚀"


# Run locally
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
