from channels.generic.websocket import AsyncWebsocketConsumer


class TrainsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('trains', self.channel_name)
        await self.accept()
    
    async def disconnect(self):
        await self.channel_layer.group_discard('trains', self.channel_name)

    async def send_trains(self, event):
        text_message = event['text']

        await self.send(text_message)
