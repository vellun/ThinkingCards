import json
import channels.generic.websocket


class LobbyConsumer(channels.generic.websocket.AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope["url_route"]["kwargs"]["uid"]
        self.room_group_name = f"lobby_{self.room_id}"

        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    async def add_user(self, event):
        username = event["username"]
        await self.send(
            text_data=json.dumps(
                {
                    "username": username,
                },
            ),
        )

