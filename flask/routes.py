from app import app, db
from flask import request, jsonify
from models import User, Expense
from datetime import datetime


TEMP_USER_ID = 123456

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


@app.route("/api/expenses", methods=["POST"])
def add_expense():
    data = request.get_json()
    date = datetime.strptime(data["date"], "%Y-%m-%d").date()
    user_id = TEMP_USER_ID
    expense = Expense(date=date, description=data["description"], category=data["category"], amount=data["amount"], user_id=user_id)

    db.session.add(expense)
    db.session.commit()

    return jsonify({"message": "Expense saved successfully"})


@app.route("/api/expenses", methods=["GET"])
def get_expenses():
    user_id = TEMP_USER_ID
    expenses = Expense.query.filter_by(user_id=user_id).all()
    expenses_list = []
    for expense in expenses:
        expenses_dict = {
            "id": expense.id,
            "date": expense.date.strftime("%Y-%m-%d"),
            "description": expense.description,
            "category": expense.category,
            "amount": expense.amount
        }
        expenses_list.append(expenses_dict)

    return jsonify(expenses=expenses_list)