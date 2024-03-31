import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'
        self.group_id = self.scope['url_route']['kwargs'].get('group_id')
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        
    def receive(self, text_data):
        text_data_json=json.loads(text_data)
        message=text_data_json['message']

        from .views import save_data
        print("save data")
        msg=save_data(message)
        print('ndesaaa',msg.host.id)
        
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                'type':'chat_message',
                'message':msg,
            }
        )
    
    def chat_message(self,event):
        print("sending the message ")
        message=event['message']
        print(message.created)
        print(message.host.username)
        print(str(message.created))
        self.send(
            text_data=json.dumps({
                'type':'chat',
                'message':message.body,
                'username':message.host.username,
                'msg_host_id':message.host.id,
                'time':str(message.created),
            })
        )

class ChatDm(WebsocketConsumer)    :
    def connect(self):
        self.room_group_name=self.scope['url_route']['kwargs']['group_id']
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
    def receive (self,text_data):
        data=json.loads(text_data)
        # message=data['message']
        group_id=data['group_id']
        # sender=data['sender']
        # receiver=data['receiver']
        print(data)
        from .views import private
        data1 = private(data)
        print("Our dadta,",data1.body)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                'type':'chat_message',
                'message':data1.body,
            }
        )
        
    def chat_message(self,event):
            print("sending the message")
            message=event['message']
            print(message)
            self.send(
                text_data=json.dumps({
                    'type':'chat',
                    'message':message,
                })
            )

        