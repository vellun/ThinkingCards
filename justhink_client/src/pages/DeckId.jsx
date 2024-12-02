import React, { useEffect, useState } from "react";
import CardSlider from "../components/UI/CardSlider/CardSlider";
import DeckService from "../API/DeckService";
import { useParams } from "react-router-dom";
import { useFetching } from "../hooks/useFetching";
import Modal from "../components/UI/Modal/Modal";
import GroupService from "../API/GroupService";

const DeckId = () => {
  const params = useParams();
  const [deck, setDeck] = useState({});
  const [modal, setModal] = useState(false);
  const [groups, setGroups] = useState([]);

  const [fetchDeckById, isLoading, error] = useFetching(async () => {
    const response = await DeckService.getById(params.id);
    setDeck(response.data);
  });

  const [fetchGroups, grLoading, grError] = useFetching(async () => {
    const response = await GroupService.getAllUsersGroups();
    setGroups(response.data);
  });

  useEffect(() => {
    fetchDeckById();
    fetchGroups();
  }, []);
  return (
    <div>
      {/* <CardSlider /> */}
      {deck.name}
      <button onClick={() => setModal(true)}>Играть</button>
      <Modal visible={modal} setVisible={setModal}>
        {groups.map((group, id) => (
          <div key={id}>
            <h5>{group.name}</h5>
          </div>
        ))}
      </Modal>
    </div>
  );
};

export default DeckId;
