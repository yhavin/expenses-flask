import React, { useState } from "react";
import LoginForm from "../components/LoginForm";

const Home = () => {

  const emptyLogin = { username: "", password: "" }

  const [loginAttempt, setLoginAttempt] = useState(emptyLogin);
  const [currentUser, setCurrentUser] = useState();

  const handleInput = (e) => {
    const { name, value } = e.target;
    setLoginAttempt({ ...loginAttempt, [name]: value })
  };

  const handleLogin = (e) => {
    e.preventDefault();
    fetch("http://127.0.0.1:5000/api/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(loginAttempt)
    })
    .then(response => response.json())
    .then(data => {
      setCurrentUser(data.username);
      console.log(data);
      setLoginAttempt(emptyLogin);
    })
    .catch(error => {
      console.error("Error:", error)
    });
  };

  return (
    <div>
      <h1>Welcome to expense tracking{currentUser ? ", " + currentUser : ""}</h1>
      <LoginForm 
        loginAttempt={loginAttempt}
        handleInput={handleInput}
        handleLogin={handleLogin}
      />
    </div>
  )
}

export default Home;