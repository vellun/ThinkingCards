import React, { useEffect, useState } from "react";
import LobbyService, { UsersService } from "../API/GameService";
import { useParams } from "react-router-dom";

const LobbyUsers = () => {
  const [users, setUsers] = useState([]);
  const [userInfo, setUserInfo] = useState([]);
  const [socket, setSocket] = useState(null);
  const params = useParams();

  async function fetchUsers() {
    const response = await LobbyService.getLobbyUsers(params.uid);
    setUsers(response.data);
  }

  async function fetchUserInfo() {
    const response = await UsersService.getUsersInfo(params.uid);
    setUserInfo(response.data);
  }

  useEffect(() => {
    fetchUsers();
    fetchUserInfo();
    const usersSocket = new WebSocket(`ws://localhost:8000/ws/${params.uid}/`);
    console.log(usersSocket);
    usersSocket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setUsers((prevUsers) => {
        if (!prevUsers.includes(data.username)) {
          return [...prevUsers, data.username];
        }
        return prevUsers;
      });
    };
    setSocket(usersSocket);

    return () => {
      usersSocket.close();
    };
  }, []);

  const sendMessage = (message) => {
    if (socket) {
      socket.send(JSON.stringify({ message }));
    }
  };

  return (
    <div>
      {users.map((user, id) => (
        <div key={id}>
          <h5>{user}</h5>
        </div>
      ))}
      {userInfo["role"] === "owner" && <button>Начать игру</button>}
      {/* <button onClick={() => sendMessage('New user joined')}>Join Lobby</button> */}
    </div>
  );
};

export default LobbyUsers;
