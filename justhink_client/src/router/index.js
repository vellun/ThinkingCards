import { Navigate } from "react-router-dom";
import DeckId from "../pages/DeckId";
import Decks from "../pages/Decks";
import Home from "../pages/Home";
import Lobby from "../pages/Lobby";
import Login from "../pages/Login";
import Register from "../pages/Register";

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
  { path: "/decks", element: <Decks /> },
  { path: "/decks/:id", element: <DeckId /> },
  { path: "/lobby/:uid", element: <Lobby /> },
];
