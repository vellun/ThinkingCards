import React, { useEffect, useState } from "react";
import DeckService from "../API/DeckService";
import DeckList from "../components/DeckList";
import { useFetching } from "../hooks/useFetching";

const Decks = () => {
  const [decksList, setDecksList] = useState([]);

  const [fetchDecks, isLoading, error] = useFetching(async () => {
    const response = await DeckService.getAll();
    setDecksList(response.data);
  });

  useEffect(() => {
    fetchDecks();
  }, []);
  return (
    <div>
      <DeckList decks={decksList} />
    </div>
  );
};

export default Decks;
