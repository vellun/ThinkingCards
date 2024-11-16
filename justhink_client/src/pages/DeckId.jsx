import React, { useEffect, useState } from "react";
import CardSlider from "../components/UI/CardSlider/CardSlider";
import DeckService from "../API/DeckService";
import { useParams } from "react-router-dom";
import { useFetching } from "../hooks/useFetching";

const DeckId = () => {
  const params = useParams();
  const [deck, setDeck] = useState({});

  const [fetchDeckById, isLoading, error] = useFetching(async () => {
    const response = await DeckService.getById(params.id);
    setDeck(response.data);
  });

  useEffect(() => {
    fetchDeckById();
  }, []);
  return (
    <div>
      {/* <CardSlider /> */}
      {deck.name}
      <button>Играть</button>
    </div>
  );
};

export default DeckId;
