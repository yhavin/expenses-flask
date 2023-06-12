import requests
from pprint import pprint


LOCALHOST = "http://127.0.0.1:5000"

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
        {"date": "2023-06-13", "description": "Footy tickets", "category": "Entertainment", "amount": 64.70},
        {"date": "2023-06-14", "description": "Park pass", "category": "Travel", "amount": 25},
        {"date": "2023-06-15", "description": "Netflix", "category": "Subscriptions", "amount": 9.99}
    ]
    index = 2
    response = requests.post(LOCALHOST + path, json=test_expenses[index])
    assert response.status_code == 200
    # pprint(response)
