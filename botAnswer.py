import json
import api
import menuList

def bot_answer(cid, mid, text):
    requ = text.split('&')
    request = {}
    for req in requ:
        request[req.split('=')[0]] = req.split('=')[1]

    textg = menuList.redirect(city = request['city'], menu= request['menu'])

    answer = api.NewMessage(text = ---, chat_id = cid, message_id= mid, buttons = )



def bot_init(cid,text):
    if text == '/start':
        with open('cities.json', 'r') as f:
            cList = json.load(f)
        cKeyboard = []

        for city in cList:
            cbut = api.Inline_button(city, city_tag)
            cKeyboard.append(cbut)

        kb = api.Inline_keyboard(*cKeyboard)
        kb = kb.requestGenerator()
        answer = api.CityMessage(text = kb, chat_id = cid)
        return(answer)

    elif text == '/admin':
        pass

    else:
        answer = api.WrongCommand(chat_id=cid)
        return(answer)

def city_tag(val):
    with open('cities.json', 'r') as f:
        cList = json.load(f)
    return(cList[val])

if __name__ == '__main__':
    bot_init('/start')
