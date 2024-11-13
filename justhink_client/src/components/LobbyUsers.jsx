import React, { useEffect, useState } from "react";
import LobbyService from "../API/GameService";
import { useParams } from "react-router-dom";

const LobbyUsers = () => {
  const [users, setUsers] = useState([]);
  const params = useParams();

  async function fetchUsers() {
    const response = await LobbyService.getLobbyUsers(params.uid);
    setUsers(response.data);
  }

  useEffect(() => {
    fetchUsers();
  }, []);

  return (
    <div>
      {users.map((user, id) => (
        <div key={id}>
          <h5>{user}</h5>
        </div>
      ))}
    </div>
  );
};

export default LobbyUsers;
