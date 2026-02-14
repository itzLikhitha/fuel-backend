from flask import Flask
from models import db
from routes.auth_routes import auth_bp
from routes.fuel_routes import fuel_bp
from routes.mechanic_routes import mechanic_bp

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(fuel_bp)
app.register_blueprint(mechanic_bp)

@app.route('/')
def home():
    return "Backend running successfully"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
