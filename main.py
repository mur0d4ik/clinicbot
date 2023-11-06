import logging
# from config import API_TOKEN
from aiogram import Bot, Dispatcher, executor, types
from button import *
from config import *


bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands = 'start')
async def lang_menu(message : types.Message):
    await message.answer(text = f'Salom {message.from_user.full_name}\nTilni tanlang!', reply_markup = main_menu)
    
    
@dp.message_handler(text = 'Uzbek🇺🇿')
async def call(message :types.Message):
    await message.answer(text = 'Nomeringizni yuboring!', reply_markup = contact)
    
    
@dp.message_handler(content_types="contact")
async def kasallik(message : types.Message):
    await message.answer(f'Sizni qaysi kasallik bezovta qilyapti?', reply_markup = await kasallik_())
    
    
@dp.message_handler(text = 'Qandli diabet')
async def kasallik(message : types.Message):
    await message.answer(f'Sizda qandli diabetning nechanchi turi?', reply_markup = await tiplar_())
    
    
@dp.message_handler(text = 'I tip')
async def kasallik(message : types.Message):
    await message.answer(f'Mumkinmas')
    
    
@dp.message_handler(text = 'II tip')
async def kasallik(message : types.Message):
    await message.answer(f'Yoshingiz nechida?')
    

# @dp.message_handler()
# async def yosh(message : types.Message):
#     global yosh
#     yosh = message.text
#     await message.answer(f"Kasallika necha yil bo'ldi?")


@dp.message_handler(text = 'Bilmayman💁‍♂️')
async def kasallik(message : types.Message):
    await message.answer(f'Yoshingiz nechida?', reply_markup = await yosh_())
    

@dp.message_handler(text = '25 va unadan yuqori')
async def yosh(message : types.Message):
    await message.answer(f"Kasalik aniqlangan kundan boshlab insulinga o'tganmisiz", reply_markup = await javob_2())


@dp.message_handler(text = 'XA')
async def kasallik(message : types.Message):
    await message.answer(f"Mumkinmas")
    
    
@dp.message_handler(text = 'YOQ')
async def kasallik(message : types.Message):
    await message.answer(f"Vazn va bo'yingiz qancha?")
    

@dp.message_handler()
async def kasallik(message : types.Message):
    await message.answer(f"Qayerdansiz?")
    
    
@dp.message_handler()
async def kasallik(message : types.Message):
    await message.answer(f"Tez orada mutaxasis siz bilan bog'lanadi")


@dp.message_handler(text = 'Xa')
async def kasallik(message : types.Message):
    await message.answer(f"Vazn va bo'yingiz nechida?")
    
    
@dp.message_handler()
async def ukol(message : types.Message):
    await message.answer(f"Insulin uklon boshlandimi?", reply_markup = await javob_())



    
    
# @dp.message_handler()
# async def kasallik(message : types.Message):
#     await message.answer(f"Tez orada siz bilan mutaxasis bog'lanadi")
    
    


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)