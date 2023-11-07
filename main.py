from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from button import *
from config import *
from state import *

storage = MemoryStorage()

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage = storage)
state = FSMContext



@dp.message_handler(commands='start')
async def lang_menuf(message: types.Message):
    await message.answer('Tilni tanglang!', reply_markup=lang)


@dp.message_handler(text = 'Uzbek🇺🇿')
async def phone_numf(message : types.Message):
    await message.answer('Telefon raqamingizni yuboring!', reply_markup = phone_number)
    await User.phone.set()


@dp.message_handler(content_types = 'contact', state = User.phone)
async def diseasef(message : types.Message, state: FSMContext):
    phone_number = message.contact['phone_number']
    await state.update_data(phone = phone_number)
    await message.answer('Sizni qaysi kasallik bezovta qilyapti?', reply_markup = await diseaseF())
    await User.disease.set()


@dp.message_handler(text = 'Qandli diabet',state = User.disease)
async def disease_typef(message: types.Message, state: FSMContext):
    disease_user = message.text
    await state.update_data(disease = disease_user)
    await message.answer('Sizda qandli diabetning nechanchi turi?', reply_markup = await disease_typeF())
    await User.disease_type.set()


@dp.message_handler(text = 'II - tip', state = User.disease_type)
async def disease_typesf(message: types.Message, state: FSMContext):
    disease_type_user = message.text
    await state.update_data(disease_type = disease_type_user)
    await message.answer('Yoshingiz nechida?', reply_markup = types.ReplyKeyboardRemove())
    await User.age_type2.set()


@dp.message_handler(state = User.age_type2)
async def age_userf(message: types.Message, state: FSMContext):
    age_user = message.text
    await state.update_data(age_type2 = age_user)
    await message.answer('Kasallikka necha yil bo\'ldi?')
    await User.year_type2.set()


@dp.message_handler(state = User.year_type2)
async def injectionf(message: types.Message, state: FSMContext):
    answer_user = message.text
    await state.update_data(answer_type2 = answer_user)
    await message.answer('Insulin ukol boshlandimi?', reply_markup = await answerF())
    await User.weight_type2.set()


@dp.message_handler(state = User.weight_type2)
async def weightf(message: types.Message, state: FSMContext):
    weight_user = message.text
    await state.update_data(weight_type2 = weight_user)
    await message.answer('Vaziningizni yozing!', reply_markup = types.ReplyKeyboardRemove())
    await User.height_type2.set()


@dp.message_handler(state = User.height_type2)
async def heightf(message: types.Message, state = FSMContext):
    heigth_user = message.text
    await state.update_data(height_type2 = heigth_user)
    await message.answer('Bo\'yingizni yozing!')
    



    


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
