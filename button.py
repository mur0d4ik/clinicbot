from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


lang = ReplyKeyboardMarkup(resize_keyboard = True).add(KeyboardButton(text = 'Uzbek🇺🇿'))

phone_number = ReplyKeyboardMarkup(resize_keyboard = True).add(KeyboardButton(text = 'Telefon raqamni yuborish☎️', request_contact = True))





disease_list = ['Qandli diabet', 'Semizlik']

async def diseaseF():
    buttons = ReplyKeyboardMarkup(resize_keyboard = True)

    for i in disease_list:
        buttons.insert(KeyboardButton(i))

    return  buttons





disease_type_list = ['I - tip', 'II - tip', 'Bilmayman🤷‍♂️']

async def disease_typeF():
    buttons = ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)

    for i in disease_type_list:
        buttons.insert(i)

    return buttons






answer_list = ['XA', 'YOQ']

async def answerF():
    buttons = ReplyKeyboardMarkup(resize_keyboard = True)

    for i in answer_list:
        buttons.insert(KeyboardButton(i))

    return buttons


answer_list2 = ['Xa', 'Yoq']

async def answer2F():
    buttons = ReplyKeyboardMarkup(resize_keyboard = True)

    for i in answer_list2:
        buttons.insert(KeyboardButton(i))

    return buttons


year_list = ['1-25 yoshgacha', '25 va undan yuqori']


async def yearF():
    buttons = ReplyKeyboardMarkup(resize_keyboard = True)

    for i in year_list:
        buttons.insert(KeyboardButton(i))

    return buttons



location = ReplyKeyboardMarkup(resize_keyboard = True)

async def loc():
    location.add('Locatsiya yuborish')

    return location
