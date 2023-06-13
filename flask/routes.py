from app import app, db
from flask import request, jsonify, send_from_directory
from models import User, Expense
from datetime import datetime


TEMP_USER_ID = 123456

# Serve static Flask app
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_frontend(path):
    return send_from_directory(app.static_folder, "index.html")


# Catch all serving for static files
@app.route("/assets/<path:filename>")
def serve_assets(filename):
    return send_from_directory("../react/dist/assets", filename)


@app.route("/")
def home():
    return "Welcome to expense tracking."


@app.route("/api/register", methods=["POST"])
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
    expense = Expense(date=date, description=data["description"], category=data["category"], amount=data["amount"], user_id=user_id, deleted=False)

    db.session.add(expense)
    db.session.commit()

    return jsonify({"message": "Expense saved successfully"}), 201


@app.route("/api/expenses", methods=["GET"])
def get_expenses():
    user_id = TEMP_USER_ID
    expenses = Expense.query.filter_by(user_id=user_id, deleted=False).all()
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

    return jsonify(expenses=expenses_list), 200


@app.route("/api/expenses/<id>", methods=["DELETE"])
def delete_expense(id):
    user_id = TEMP_USER_ID
    expense = Expense.query.filter_by(id=id).first()
    
    if not expense:
        return jsonify({"message": f"There is no expense with ID {id}"}), 404
    
    expense.deleted = True
    db.session.commit()

    return jsonify({"message": f"Expense {id} successfully marked as deleted"}), 204