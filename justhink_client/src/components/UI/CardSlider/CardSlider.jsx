import React from "react";
import Slider from "react-slick";
import { useState, useEffect } from "react";
import classes from "./CardSlider.module.css";
import axios from "axios";
import CardService from "../../../API/CardService";
import { useParams } from "react-router-dom";

const cards = [
  "Часть тела человека или животного",
  "Гора, река, озеро или море",
  "Можно положить в карман",
  "Женское имя",
  "Женщина-секс-символ",
];

const CardSlider = () => {
  const [cardsList, setCardsList] = useState([]);

  const params = useParams()

  async function fetchCards() {
    const response = await CardService.getById(params.id)
    setCardsList(response.data);
  }

  useEffect(() => {
    fetchCards();
  }, []);

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
    <div>
      {" "}
      <button onClick={fetchCards}>get cards</button>
      <Slider className="slider" {...settings}>
        {cardsList.map((card, idx) => (
          <div key={idx}>
            <div
              className={
                idx === cardIndex
                  ? `${classes.card} ${classes.activeCard}`
                  : classes.card
              }
            >
              <div className={classes.cardContent}>{card.text}</div>
            </div>
          </div>
        ))}
      </Slider>
    </div>
  );
};

export default CardSlider;
