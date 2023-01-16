import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from "./pages/Home";
import TodoListPage from "./pages/TodoList";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/todolist/:id" element={<TodoListPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
