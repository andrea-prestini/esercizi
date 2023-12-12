import "./App.css";

function App() {
  return (
    <>
      <h1>Todo List</h1>
      <div className="card">
        <form>
          <input type="text" />
          <button type="submit">Add Todo</button>
        </form>
        <ul className="todos">
          <li className="todo">
            <span>Todo Name</span>
            <button>Delete</button>
          </li>
        </ul>
      </div>
    </>
  );
}

export default App;
