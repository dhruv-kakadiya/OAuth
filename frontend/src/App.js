import axios from "axios";
import './App.css';
import React, {useEffect} from 'react';

function App() {

  useEffect(() => {
    fetch("http://localhost:8000/accounts/csrf-token/")
      .then((response) => response.json())
      .then((data) => {
        const token = data.csrftoken;
        console.log("CSRF-Token: ", token);
    });
  }, [])

  const logIn = () => {
    fetch("http://localhost:8000/accounts/get-auth-url/")
      .then((response) => response.json())
      .then((data) => {
        window.location.replace(data.uri);
    });
  }


  const logOut = () => {
    fetch("http://localhost:8000/accounts/logout/")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
    });
  }

  const home = () => {
    axios.get("http://localhost:8000/accounts/home/", { credentials : 'same-origin' })
    .then((response) => {
    // handle success
      console.log(response);
    })
  }


  return (
    <div className="App">
      <button type="button" onClick={logIn}>Log In</button>
      <button type="button" onClick={logOut}>Log Out</button>
      <button type="button" onClick={home}>Home</button>
    </div>
  );
}

export default App;
