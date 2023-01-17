import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

const TodoList = () => {
  const params = useParams();

  const [todo, setTodo] = useState([]);
  const [error, setError] = useState(null);
  const [addTodo, setAddTodo] = useState({});

  const onChange = (e) => {
    const { name, value } = e.target;
    setAddTodo((current) => ({
      ...current,
      [name]: value,
    }));
  };

  const getTodo = async () => {
    const response = await fetch(
      `http://127.0.0.1:8000/api/todo-list/${params?.id}/todos/`
    );
    const data = await response.json();
    setTodo(data);
  };

  const postTodo = async (e) => {
    e.preventDefault();

    var headers = new Headers();
    headers.append("Content-Type", "application/json");

    var body = JSON.stringify({ ...addTodo, todo_list: params?.id });

    const response = await fetch("http://127.0.0.1:8000/api/todo/", {
      body,
      headers,
      method: "POST",
    });

    if (response.ok) {
      setError(null);
      setAddTodo({});
      getTodo();
    } else {
      const data = await response.json();
      setError(data);
    }
  };

  const patchTodo = async (id, is_completed) => {
    var headers = new Headers();
    headers.append("Content-Type", "application/json");

    var body = JSON.stringify({ is_completed });

    const response = await fetch(`http://127.0.0.1:8000/api/todo/${id}/`, {
      body,
      headers,
      method: "PATCH",
    });
    const data = await response.json();
    console.log(data);
    getTodo();
  };

  const deleteTodo = async (id) => {
    await fetch(`http://127.0.0.1:8000/api/todo/${id}/`, {
      method: "DELETE",
    });
    getTodo();
  };

  useEffect(() => {
    getTodo();
  }, []);

  return (
    <div className="container mt-3">
      {error && (
        <div className="alert alert-danger fade show" role="alert">
          {error.error}
        </div>
      )}
      <form onSubmit={postTodo}>
        <div className="row">
          <div className="col">
            <input
              name="title"
              value={addTodo.title ?? ""}
              onChange={onChange}
              className="form-control mb-2"
              placeholder="Titulo"
            />
            <input
              name="description"
              value={addTodo.description ?? ""}
              onChange={onChange}
              className="form-control mb-2"
              placeholder="Descripción"
            />
            <button className="btn btn-sm btn-primary" type="submit">
              Agregar
            </button>
          </div>
        </div>
      </form>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Titulo</th>
              <th scope="col">Fecha</th>
              <th scope="col">Acciones</th>
            </tr>
          </thead>
          <tbody>
            {todo.map((todo) => (
              <tr key={todo.id}>
                <td scope="row">{todo.id}</td>
                <td>
                  {todo.title} <br /> {todo.description}
                </td>
                <td>{todo.created_at}</td>
                <td>
                  <button
                    className="btn btn-sm btn-link"
                    onClick={() => patchTodo(todo.id, !todo.is_completed)}
                  >
                    <img
                      src={
                        todo.is_completed
                          ? "/check-circle-fill.svg"
                          : "/check-circle.svg"
                      }
                      alt="Bootstrap"
                      width="20"
                      height="20"
                    />
                  </button>
                  <button
                    className="btn btn-sm btn-link"
                    onClick={() => deleteTodo(todo.id)}
                  >
                    <img
                      src="/trash-fill.svg"
                      alt="Bootstrap"
                      width="20"
                      height="20"
                    />
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default TodoList;
