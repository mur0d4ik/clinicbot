from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


main_menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = 'Uzbek🇺🇿')
        ]
    ],
    resize_keyboard = True
)


contact = ReplyKeyboardMarkup(
    keyboard = [  
        [
            KeyboardButton('Nomeringizni yuboring ☎️', request_contact=True)
        ]
    ],
    resize_keyboard = True
)


kasallik = ['Qandli diabet','Semizlik']


async def kasallik_():
    buttons = ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
    
    for i in kasallik:
        buttons.insert(KeyboardButton(text = i))    
        
    return buttons


tiplar = ['I tip', 'II tip', 'Bilmayman💁‍♂️']


async def tiplar_():
    buttons = ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
    
    for i in tiplar:
        buttons.insert(KeyboardButton(text = i)) 
        
    return buttons


javob = ['Xa', 'Yoq']
javob2 = ['XA', 'YOQ']

async def javob_():
    buttons = ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
    
    for i in javob:
        buttons.insert(KeyboardButton(text = i))
        
    return  buttons


async def javob_2():
    buttons = ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
    
    for i in javob2:
        buttons.insert(KeyboardButton(text = i))
        
    return  buttons


yosh = ['1 - 25 yoshgacha', '25 va unadan yuqori']


async def yosh_():
    buttons = ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
        
    for i in yosh:
        buttons.insert(KeyboardButton(text = i))
        
    return buttons 