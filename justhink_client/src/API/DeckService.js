import api from "../api";

export default class DeckService {
  static async getAll() {
    const response = await api.get(`/api/decks/`);
    return response;
  }

  static async getById(id) {
    const response = await api.get(`/api/decks/${id}/`);
    return response;
  }
}
