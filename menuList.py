import api
import botAnswer
import requests
import json

def redirect(menu, city):
    if menu == 'Help_Menu':
        return(helpMenu(city))
    if menu == 'Call':
        return(call(city))

def helpMenu(city):
    but3 = api.Inline_button(text='Изменить город', ans = 'City={}&Menu=City_Change'.format(city))
    but2 = api.Inline_button(text='Заказать звонок', ans = 'City={}&Menu=Call'.format(city))
    but1 = api.Inline_button(text='Перейти в магазн', ans = 'City={}&Menu=Shop_Menu'.format(city))
    text = 'Вы в меню помощи, выберите функцию:'
    return ({'text': text,'keyboard': [but1, but2, but3]})


def call(city):
    text = 'отправьте свой номер в формате 7xxxxxxxxxx'
    but3 = api.Inline_button(text='Изменить город', ans='City={}&Menu=City_Change'.format(city))
    but2 = api.Inline_button(text='Заказать звонок', ans='City={}&Menu=Call'.format(city))
    but1 = api.Inline_button(text='Перейти в магазн', ans='City={}&Menu=Shop_Menu'.format(city))

    return ({'text': text, 'photo': './test.png', 'keyboard': [but1, but2, but3]})