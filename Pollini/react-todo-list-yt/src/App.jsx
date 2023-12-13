import { useState } from "react";
import "./App.css";

function App() {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState("");

  const handleNewTodoChange = (event) => {
    setNewTodo(event.target.value);
    console.log(newTodo);
  };

  const handleAddTodo = (event) => {
    event.preventDefault();
    if (newTodo === "") return;
    setTodos([...todos, newTodo]);
    setNewTodo("");
    console.log(todos);
  };

  const hadleTodoDelete = (index) => {
    const newTodos = [...todos];
    newTodos.splice(index, 1);
    setTodos(newTodos);
  };

  return (
    <>
      <h1>Todo List</h1>
      <div className="card">
        <form>
          <input type="text" value={newTodo} onChange={handleNewTodoChange} />
          <button type="submit" onClick={handleAddTodo}>
            Add Todo
          </button>
        </form>
        <ul className="todos">
          {todos.map((todo, index) => (
            <li className="todo" key={index}>
              <span>{todo}</span>
              <button onClick={() => hadleTodoDelete(index)}>Delete</button>
            </li>
          ))}
        </ul>
      </div>
    </>
  );
}

export default App;
