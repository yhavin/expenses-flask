from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///expenses.db"
db = SQLAlchemy(app)

# Keep import after app creation to avoid circular import
import routes