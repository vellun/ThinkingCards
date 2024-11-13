import React from "react";
import LobbyService from "../API/GameService";
import { useNavigate } from "react-router-dom";

const Home = () => {
  const navigate = useNavigate();

  async function goToLobby() {
    const response = await LobbyService.getLobbyId();
    navigate(`/lobby/${response.data.uuid}/`);
  }
  return (
    <div>
      <button onClick={goToLobby}>В лобби</button>
    </div>
  );
};

export default Home;
