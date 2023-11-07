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