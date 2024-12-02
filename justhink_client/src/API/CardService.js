import api from "../api";

export default class CardService {
  static async getById(id) {
    const response = await api.get(`/api/decks/${id}/cards/`);
    return response;
  }
}
