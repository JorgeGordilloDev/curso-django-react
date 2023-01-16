import { Link } from "react-router-dom";

const Todo = ({ todo }) => {
  return (
    <div className="col">
      <div className="card h-100">
        <div className="card-body">
          <Link to={`/todolist/${todo.id}`}>
            <h5 className="card-title">{todo.name}</h5>
          </Link>
          <p className="card-text">{todo.description}</p>
        </div>
        <div className="card-footer">
          <small className="text-muted">
            Ultima modificación {todo.updated_at}
          </small>
        </div>
      </div>
    </div>
  );
};

export default Todo;
