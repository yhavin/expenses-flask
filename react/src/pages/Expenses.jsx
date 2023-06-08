import React, { useState, useEffect } from "react";
import axios from "axios";

const Expenses = () => {
  const [expenses, setExpenses] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/expenses")
    .then(response => response.json())
    .then(data => {
      console.log(data);
      setExpenses(data.expenses)
    })
  }, [])

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
    </div>
  )
}

export default Expenses;