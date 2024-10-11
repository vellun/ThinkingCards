import React from "react";
import Slider from "react-slick";
import { useState } from "react";
import classes from "./CardSlider.module.css";
import axios from "axios";

const cards = [
  "Часть тела человека или животного",
  "Гора, река, озеро или море",
  "Можно положить в карман",
  "Женское имя",
  "Женщина-секс-символ",
];

const CardSlider = () => {
//   const [cards, setCards] = useState([]);

  async function fetchCards() {
    const response = await axios.get(
      "http://127.0.0.1:8000/api/v1/decks/1/cards/"
    );
    console.log(response.data)
  }

  const [cardIndex, setCardIndex] = useState(0);

  const settings = {
    infinite: true,
    speed: 300,
    slidesToShow: 3,
    centerMode: true,
    centerPadding: 0,
    beforeChange: (current, next) => setCardIndex(next),
  };

  return (
    <div> <button onClick={fetchCards}>get cards</button>
    <Slider className="slider" {...settings}>
      {cards.map((card, idx) => (
        <div>
          <div
            className={
              idx === cardIndex
                ? `${classes.card} ${classes.activeCard}`
                : classes.card
            }
          >
            <div className={classes.cardContent}>{card}</div>
          </div>
        </div>
      ))}
    </Slider>
    </div>
  );
};

export default CardSlider;
