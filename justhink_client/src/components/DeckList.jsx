import React from "react";

const DeckList = ({ decks }) => {
  if (!decks.length) {
    return <h1 style={{ textAlign: "center" }}>Колоды не найдены!</h1>;
  }
  return (
    <div>
      {decks.map((deck, id) => (
        <div key={id}>
          <a href={`/decks/${deck.id}`}><h5>{deck.name}</h5></a>
        </div>
      ))}
    </div>
  );
};

export default DeckList;
