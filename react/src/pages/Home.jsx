import React, { useState } from "react";
import LoginForm from "../components/LoginForm";

const Home = () => {

  const emptyLogin = { username: "", password: "" }

  const [loginAttempt, setLoginAttempt] = useState(emptyLogin);

  const handleInput = (e) => {
    const { name, value } = e.target;
    setLoginAttempt({ ...loginAttempt, [name]: value })
  };

  return (
    <div>
      <h1>Welcome to expense tracking</h1>
      <LoginForm 
        loginAttempt={loginAttempt}
        handleInput={handleInput}
      />
    </div>
  )
}

export default Home;