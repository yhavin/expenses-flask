from app import app, db
from flask import request, jsonify
from models import User, Expense


@app.route("/")
def home():
    return "Welcome to expense tracking."

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"message": "Username is already taken"}), 409
    
    user = User(username=username)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": f"User {username} registered successfully"}), 201
