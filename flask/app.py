from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__, static_folder="../react/dist")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///expenses.db"
db = SQLAlchemy(app)

# Following CORS lines added to avoid CORS errors
CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

# Keep import after app creation to avoid circular import
import routes