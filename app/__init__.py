from flask import Flask
from flaskext.mysql import MySQL
from config import Config
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# Configuration de la base de données MySQL
app.config['MYSQL_DATABASE_HOST'] = Config.MYSQL_HOST
app.config['MYSQL_DATABASE_USER'] = Config.MYSQL_USER
app.config['MYSQL_DATABASE_PASSWORD'] = Config.MYSQL_PASSWORD
app.config['MYSQL_DATABASE_DB'] = Config.MYSQL_DB

CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5000/"}})

mysql = MySQL()
mysql.init_app(app)

from app.routes import user_route, administrator_route, medecin_route, session_route, avis_route, prescription_route

app.register_blueprint(user_route.user_bp, url_prefix='/api/user')
app.register_blueprint(administrator_route.admin_bp, url_prefix='/api/admin')
app.register_blueprint(medecin_route.medecin_bp, url_prefix='/api/medecin')
app.register_blueprint(session_route.session_bp, url_prefix='/api/session')
app.register_blueprint(avis_route.avis_bp, url_prefix='/api/avis')
app.register_blueprint(prescription_route, url_prefix='/api/prescription')

