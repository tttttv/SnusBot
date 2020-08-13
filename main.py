import requests
import json
import flask

import api

app = flask.Flask(__name__)
URL = 'https://api.telegram.org/bot1289820254:AAG6J2Q3L7oOC_4CRjOmKxYtCQuUnRPnOy8/'
### https://api.telegram.org/bot1289820254:AAG6J2Q3L7oOC_4CRjOmKxYtCQuUnRPnOy8/setWebhook?url=https://38e5913f5423.ngrok.io


def log(req):
    with open('request.json', 'w') as f:
        json.dump(req, f, indent=2)

def send_message(id,message):
    answer = {'chat_id': id, 'text': message}
    res = requests.post(URL + 'sendMessage', json=answer)
    return(res.json()) #возвращает ['ok'] : True

@app.route('/', methods=['POST','GET'])
def main():
    if flask.request.method == "POST":
        req = flask.request.get_json()
        log(req)

        send_message(req['message']['chat']['id'], 'Hi')

        return flask.jsonify(req)
    return 'Welcome'

def another_send(id,message):
    res = requests.post(URL + 'sendMessage', json=message)
    return (res.json())  # возвращает ['ok'] : True
if __name__ == '__main__':
    #app.debug=True
    #app.run()

    pid = 'https://i.pinimg.com/originals/76/6c/f7/766cf770ea8dd3529bd8e0c41d6784be.jpg'

    but1 = api.Inline_button('первая', api.foo)
    but2 = api.Inline_button('вторая', api.foo)
    ik = api.Inline_keyboard(but1, but2)
    #print(ik.requestGenerator())
    #reply_markup = {
    #   #  'inline_keyboard': [[{'text': 'текст1', 'callback_data': 'button1'}],[{'text': 'текст2','callback_data': 'button2'}]]}
    #
    #data = {'chat_id': 1178422178, 'text': 'test url', 'reply_markup': json.dumps(ik.requestGenerator())}


    #another_send(1178422178, data)

    #message = {'chat_id': 1178422178, 'text': 'Opisanie', 'reply_markup': ik.requestGenerator()}
    #message = {'chat_id': 1178422178, 'text': 'Opisanie'}

    #requests.post(URL + 'sendPhoto', data = data, files=file)
    #api.send_message(message, photo='./test.png')
