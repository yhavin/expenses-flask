import React from "react";

const LoginForm = ({ loginAttempt, handleInput }) => {
  return (
    <div>
      <h3>Login</h3>
      <form style={{ display: 'grid', rowGap: '1rem' }}>
        <div style={{ display: 'flex', alignItems: 'flex-start' }}>
          <label style={{ width: '1rem', marginRight: '1rem' }}>
            Email
            <input
              type="email"
              name="username"
              value={loginAttempt.username}
              onChange={handleInput}
            />
          </label>
        </div>
        <div style={{ display: 'flex', alignItems: 'flex-start' }}>
          <label style={{ width: '1rem', marginRight: '1rem' }}>
            Password
            <input
              type="password"
              name="password"
              value={loginAttempt.password}
              onChange={handleInput}
            />
          </label>
        </div>
      </form>
    </div>
  )
}

export default LoginForm;