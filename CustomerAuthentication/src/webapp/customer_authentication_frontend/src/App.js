import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <body>
            <form>
                <h2>Login</h2>
                <label for="username">Username: </label>
                <input type="text" id="username" name="username" required />
                    <br />
                <label for="password">Password: </label>
                <input type="password" id="password" name="password" required />
                   <br />
                <button className="login-btn" type="submit">Login</button>
            </form>
        </body>
      </header>
    </div>
  );
}

export default App;
