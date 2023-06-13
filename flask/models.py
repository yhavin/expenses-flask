from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    expenses = db.relationship("Expense", backref="user", lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(password, self.password_hash)
    
    def __repr__(self):
        return f"User(id={self.id}, username={self.username})"
    

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    description = db.Column(db.String(120), index=True)
    category = db.Column(db.String(80), index=True)
    amount = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    deleted = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"Expense(id={self.id}, description={self.description}, amount={self.amount}, user_id={self.user_id})"
    

# Uncomment to rebuild the database schema
# WARNING: DELETES ALL DATABASE DATA
# from app import app
# with app.app_context():
#     db.drop_all()
#     db.create_all()