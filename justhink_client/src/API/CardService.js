import axios from "axios";
import api from "../api";

export default class CardService {
  // static async getAll(limit = 10, page = 1) {
  //   const response = await axios.get(
  //     "https://jsonplaceholder.typicode.com/posts",
  //     {
  //       params: {
  //         _limit: limit,
  //         _page: page,
  //       },
  //     }
  //   );
  //   return response;
  // }

  static async getById(id) {
    const response = await api.get(
      `http://127.0.0.1:8000/api/decks/${id}/cards/`
    );
    return response;
  }
}
