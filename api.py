import requests
import json

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
    def __init__(self, text, func):
        self.text = text
        self.callback = func(self.text)

    def generateRequest(self):
        return([{'text': self.text, 'callback_data': self.callback}])

class Message():
    def __init__(self, chat_id, text, reply_markup = None, ):
        pass

class Photo():
    def __init__(self, path):
        pass


def foo(text):
    return('sendMessage?text=testing')


def send_message(text='Test', photo=False):
    URL = 'https://api.telegram.org/bot1289820254:AAG6J2Q3L7oOC_4CRjOmKxYtCQuUnRPnOy8/'
    if photo:
        cap = text.pop('text')
        text['caption'] = cap
        file = {'photo': open(photo, 'rb')}
        but = text.pop('reply_markup')
        requests.post(URL + 'sendPhoto?reply_markup={}'.format(json.dumps(but)), data=text, files=file)
    else:
        requests.post(URL + 'sendMessage', json=text)


if __name__ == '__main__':
    pass