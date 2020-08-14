import requests
import json
import flask
import botAnswer
import api

app = flask.Flask(__name__)
URL = 'https://api.telegram.org/bot1289820254:AAG6J2Q3L7oOC_4CRjOmKxYtCQuUnRPnOy8/'
### https://api.telegram.org/bot1289820254:AAG6J2Q3L7oOC_4CRjOmKxYtCQuUnRPnOy8/setWebhook?url=https://38e5913f5423.ngrok.io


def log(req):
    with open('log.json', 'w') as f:
        json.dump(req, f, indent=2, ensure_ascii=False)

@app.route('/', methods=['POST','GET'])  ### Обработка входящего запроса
def main():
    if flask.request.method == "POST":
        req = flask.request.get_json()
        log(req)

        try: ### Исправление сообщения
            mid = req['callback_query']['message']['message_id']
            cid = req['callback_query']['message']['chat']['id']
            tex = req['callback_query']['data']
            print('Recieved: \n', tex)

            answer = botAnswer.bot_answer(cid, mid, tex)
            answer.send_message()

        except KeyError: ### Новое сообщение
            cid = req['message']['chat']['id']
            tex = req['message']['text']
            print('Recieved: \n', tex)

            answer = botAnswer.bot_init(cid, tex)
            answer.send_message()

        return flask.jsonify(req)
    return 'Welcome'

if __name__ == '__main__':
    app.run()

