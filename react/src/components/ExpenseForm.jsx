import React from "react";

const ExpenseForm = ({ newExpense, handleInput, handleSubmit }) => {
  return (
    <div>
      <h3>Add expense</h3>
      <form onSubmit={handleSubmit} style={{ display: 'grid', rowGap: '1rem' }}>
        <div style={{ display: 'flex', alignItems: 'flex-start' }}>
          <label style={{ width: '1rem', marginRight: '1rem' }}>
            Date
            <input
              type="date"
              name="date"
              value={newExpense.date}
              onChange={handleInput}
            />
          </label>
        </div>
        <div style={{ display: 'flex', alignItems: 'flex-start' }}>
          <label style={{ width: '1rem', marginRight: '1rem' }}>
            Description
            <input
              type="text"
              name="description"
              value={newExpense.description}
              onChange={handleInput}
            />
          </label>
        </div>
        <div style={{ display: 'flex', alignItems: 'flex-start' }}>
          <label style={{ width: '1rem', marginRight: '1rem' }}>
            Category
            <input
              type="text"
              name="category"
              value={newExpense.category}
              onChange={handleInput}
            />
          </label>
        </div>
        <div style={{ display: 'flex', alignItems: 'flex-start' }}>
          <label style={{ width: '1rem', marginRight: '1rem' }}>
            Amount
            <input
              type="number"
              name="amount"
              value={newExpense.amount}
              onChange={handleInput}
            />
          </label>
        </div>
        <button type="submit" onClick={handleSubmit} style={{ width: '8rem', justifySelf: 'start' }}>Submit</button>
      </form>
    </div>
  )
};

export default ExpenseForm;