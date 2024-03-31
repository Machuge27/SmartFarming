import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

#tukiwa free tutacode ile error na zile api ,,unaona hii text
#sawa sawa use comments
#we mzee tuanze tukisubiria chiqo
#ANZENI BILA MM ,,,fty chiqo hapo chini kuna place imeandikwa chat click hapo


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name='test'
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
        msg=save_data(message)
        print('ndesaaa',msg.host.id)
        
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                'type':'chat_message',
                'message':msg,
            }
        )
    
    def chat_message(self,event):
        print("sendin the message ")
        message=event['message']
        print(message.created)
        print(message.host.username)
        print(str(message.created))
        self.send(
            text_data=json.dumps({
                'type':'chat',
                'message':message.body,
                'username':message.host.username,
                'time':str(message.created),
            })
        )

class ChatDm(WebsocketConsumer)    :
    def connect(self):
        self.room_group_name="test2"
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
            group_id,{
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
                    'message':message.body,
                })
            )

        