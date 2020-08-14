import api
import botAnswer
import requests
import json

def redirect(menu, city):
    if menu == 'Help_Menu':
        return(helpMenu(city))


def helpMenu(city):
    but1 = api.Inline_button(text='Перейти в магазн', )