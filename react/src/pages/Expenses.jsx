import React, { useState, useEffect } from "react";
import ExpenseForm from "../components/ExpenseForm";


const Expenses = () => {

  const default_expense = {
    date: "",
    description: "",
    category: "",
    amount: ""
  };

  const [expenses, setExpenses] = useState([]);
  const [newExpense, setNewExpense] = useState(default_expense);

  const handleInput = (e) => {
    const { name, value } = e.target;
    setNewExpense({ ...newExpense, [name]: value })
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("http://127.0.0.1:5000/api/expenses", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(newExpense)
    })
    .then(response => {
        setNewExpense(default_expense);
        fetchExpenses();
        console.log("Expense added successfully");
    })
    .catch(error => {
      console.error("Error:", error)
    });
  };

  const fetchExpenses = () => {
    fetch("http://127.0.0.1:5000/api/expenses")
    .then(response => response.json())
    .then(data => {
      console.log(data);
      setExpenses(data.expenses)
    })
    .catch(error => {
      console.error("Error:", error)
    });
  };

  useEffect(() => {
    fetchExpenses();
  }, []);

  return (
    <div>
      <h1>Expenses</h1>
      <table>
        <thead>
          <tr>
            <th>Date</th>
            <th>Description</th>
            <th>Category</th>
            <th>Amount</th>
          </tr>
        </thead>
        <tbody>
          {expenses.map(expense => (
            <tr key={expense.id}>
              <td>{expense.date}</td>
              <td>{expense.description}</td>
              <td>{expense.category}</td>
              <td>{expense.amount.toFixed(2)}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <ExpenseForm 
        newExpense={newExpense}
        handleInput={handleInput}
        handleSubmit={handleSubmit}
      />
    </div>
  )
}

export default Expenses;