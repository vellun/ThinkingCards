import api from "../api";

export default class LobbyService {
  static async getLobbyId() {
    const response = await api.get("/lobby/");
    return response;
  }

  static async getLobbyUsers(uid) {
    const response = await api.get(`/lobby/${uid}`);
    return response;
  }
}

export class UsersService {
  static async getUsersInfo(uid) {
    const response = await api.get(`/users/${uid}`);
    return response;
  }
}
