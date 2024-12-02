import api from "../api";

export default class GroupService {
  static async getAllUsersGroups() {
    const response = await api.get("/api/groups/");
    return response;
  }
}

