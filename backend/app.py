from flask import Flask
from flask_cors import CORS

from config import Config
from database import db
from routes.employee_routes import employee_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
CORS(app)

# Register all employee routes under /api
app.register_blueprint(employee_bp, url_prefix="/api")

@app.route("/")
def home():
    return {
        "status": "UP",
        "service": "Python CRUD Backend"
    }, 200

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)