import requests
import json
URL = 'https://api.telegram.org/bot1289820254:AAG6J2Q3L7oOC_4CRjOmKxYtCQuUnRPnOy8/'

class Inline_keyboard():
    def __init__(self,*args):
        self.buttons = []
        for button in args:
            self.buttons.append(button)

    def requestGenerator(self):
        reply_markup = {'inline_keyboard': []}
        for button in self.buttons:
            reply_markup['inline_keyboard'].append(button.generateRequest())
        return reply_markup


class Inline_button():
    def __init__(self, text, ans):
        self.text = text
        self.callback = ans

    def generateRequest(self):
        return([{'text': self.text, 'callback_data': self.callback}])


class Message():
    def __init__(self, text=False, chat_id=False, message_id=False, city=False, photo=False, keyboard=False):
        self.text = text
        self.city=city
        self.photo=photo
        self.chat_id = chat_id
        self.message_id = message_id
        self.keyboard = keyboard
        self.request = self.gen_request(text)

    def send_message(self):
        if self.photo:
            file = {'photo': open(self.photo, 'rb')}
            self.request['caption'] = self.request.pop('text')
            self.request.pop('message_id')
            if self.keyboard:
                print(self.photo)
                but = self.request.pop('reply_markup')
                requests.post(URL + 'sendPhoto', data=self.request,  files=file)
            else:
                requests.post(URL + 'sendPhoto', data=self.request, files=file)
        else:
            requests.post(URL + 'sendMessage', json=self.request)

        print('The message was sent:')
        print(self.request)


class CityMessage(Message):
    def gen_request(self, ct):
        text = {'chat_id': self.chat_id, 'text': 'Выберите город'}
        print('Keyboard: ', ct)
        text['reply_markup'] = ct
        return(text)
        #requests.post(URL + 'sendMessage?reply_markup={}'.format(ct), json=text)


class WrongCommand(Message):
    def gen_request(self, _):
        text = {'chat_id': self.chat_id, 'text': 'Нет такой команды'}
        return(text)


class NewMessage(Message):
    def __init__(self, *args, **kwargs):
        super(NewMessage, self).__init__(*args, **kwargs)
        requests.post(URL + 'deleteMessage', json={'chat_id': self.chat_id, "message_id": self.message_id})

    def gen_request(self, _):
        if self.keyboard:
            kb = Inline_keyboard(*self.keyboard)
            kb = kb.requestGenerator()

            text = {'chat_id': self.chat_id, 'text': self.text, 'message_id': self.message_id, 'reply_markup': kb}
            return(text)
        else:
            text = {'chat_id': self.chat_id, 'message_id': self.message_id, 'text': self.text}
            return(text)




def foo1(text):
    return('sendMessage?text=First')

def foo2(text):
    return('sendMessage?text=Second')

if __name__ == '__main__':
    pass

# but1 = api.Inline_button('Первая', api.foo1)
# but2 = api.Inline_button('Вторая', api.foo2)
# ik = api.Inline_keyboard(but1, but2)


# message = botAnswer.botAnswer()
# message = {'chat_id': 1178422178, 'text': 'Описание сообщения'}
# api.new_message(message)


#message = {'message_id': mid, 'chat_id': cid, 'text': 'Новое сообщение', 'reply_markup': ik.requestGenerator()}