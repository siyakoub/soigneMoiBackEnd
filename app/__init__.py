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