import { Navigate } from "react-router-dom";
import Deck from "../pages/Deck";
import Login from "../pages/Login";
import Register from "../pages/Register";
import Home from "../pages/Home";

function Logout() {
  localStorage.clear();
  return <Navigate to="/login" />;
}

function RegisterAndLogout() {
  localStorage.clear();
  return <Register />;
}

export const routes = [
  { path: "/", element: <Home /> },
  { path: "/login", element: <Login /> },
  { path: "/logout", element: <Logout /> },
  { path: "/register", element: <RegisterAndLogout /> },
  { path: "/deck", element: <Deck /> },
];
