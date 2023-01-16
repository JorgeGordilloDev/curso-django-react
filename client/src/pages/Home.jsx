import { useState, useEffect } from "react";
import Todo from "../components/Todo";

const Home = () => {
  const [todoList, setTodoList] = useState([]);
  const [addTodo, setAddTodo] = useState({});
  const [error, setError] = useState(null);

  const onChange = (e) => {
    const { name, value } = e.target;
    setAddTodo((current) => ({
      ...current,
      [name]: value,
    }));
  };

  const getTodoList = async () => {
    const response = await fetch("http://127.0.0.1:8000/api/todo-list/");
    const data = await response.json();
    setTodoList(data);
  };

  const postTodoList = async (e) => {
    e.preventDefault();

    var headers = new Headers();
    headers.append("Content-Type", "application/json");

    var body = JSON.stringify(addTodo);

    const response = await fetch("http://127.0.0.1:8000/api/todo-list/", {
      body,
      headers,
      method: "POST",
    });
    if (response.ok) {
      getTodoList();
      setError(null);
      setAddTodo({});
    } else {
      const data = await response.json();
      setError(data);
    }
  };

  useEffect(() => {
    getTodoList();
  }, []);

  return (
    <>
      <div className="container mt-4">
        {error && (
          <div className="alert alert-danger fade show" role="alert">
            {error.error}
          </div>
        )}
        <form onSubmit={postTodoList}>
          <div className="row">
            <div className="col-5">
              <input
                type="text"
                name="name"
                value={addTodo.name ?? ""}
                onChange={onChange}
                className="form-control"
                placeholder="Nombre"
              />
            </div>
            <div className="col-6">
              <input
                type="text"
                name="description"
                value={addTodo.description ?? ""}
                onChange={onChange}
                className="form-control"
                placeholder="Descripción"
              />
            </div>
            <div className="col-1">
              <button className="btn btn-primary" type="submit">
                Agregar
              </button>
            </div>
          </div>
        </form>
      </div>
      <div className="container mt-4">
        <div className="row row-cols-2 row-cols-sm-3 row-cols-md-4 g-3">
          {todoList?.map((todo) => (
            <Todo key={todo.id} todo={todo} />
          ))}
        </div>
      </div>
    </>
  );
};

export default Home;
