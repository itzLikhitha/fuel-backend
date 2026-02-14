from flask import Flask
from flask_cors import CORS
import os

# Import Blueprints
from routes.auth_routes import auth_bp
from routes.fuel_routes import fuel_bp
from routes.mechanic_routes import mechanic_bp

app = Flask(__name__)
CORS(app)

# Register Blueprints (NO extra prefix here)
app.register_blueprint(auth_bp)
app.register_blueprint(fuel_bp)
app.register_blueprint(mechanic_bp)

# Home route
@app.route("/")
def home():
    return "Fuel Delivery Backend Running Successfully!"

# Render Port Config
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
