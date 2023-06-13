import requests
from pprint import pprint


LOCALHOST = "http://127.0.0.1:5000"

# Test registering user
def test_register_user():
    path = "/api/register"
    header = {"Content-Type": "application/json"}
    test_users = [
        {"username": "john", "password": "john123"},
        {"username": "bill", "password": "bill456"},
        {"username": "tom", "password": "tom789"},
    ]
    index = 1
    response = requests.post(LOCALHOST + path, json=test_users[index])
    assert response.status_code == 201


# Test getting all expenses
def test_get_all_expenses():
    path = "/api/expenses"
    response = requests.get(LOCALHOST + path)
    assert response.status_code == 200
    # pprint(response.json())


# Test adding expense
def test_add_expense():
    path = "/api/expenses"
    header = {"Content-Type": "application/json"}
    test_expenses = [
        {"date": "2023-06-13", "description": "Footy tickets", "category": "Entertainment", "amount": 64.70, "deleted": False},
        {"date": "2023-06-14", "description": "Park pass", "category": "Travel", "amount": 25, "deleted": False},
        {"date": "2023-06-15", "description": "Netflix", "category": "Subscriptions", "amount": 9.99, "deleted": False}
    ]
    index = 2
    response = requests.post(LOCALHOST + path, json=test_expenses[index])
    assert response.status_code == 201
    # pprint(response)


# Test deleting expense
def test_delete_expense():
    id = 10
    path = f"/api/expenses/{id}"
    response = requests.delete(LOCALHOST + path)
    assert response.status_code == 204
