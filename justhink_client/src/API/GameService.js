import api from "../api";

export default class LobbyService {
  static async getLobbyId() {
    const response = await api.get("/lobby-id/");
    return response;
  }

  static async getLobbyUsers(uid) {
    const response = await api.get(`/lobby/${uid}`);
    return response;
  }
}
