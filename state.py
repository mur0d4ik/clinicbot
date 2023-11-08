from aiogram.dispatcher.filters.state import StatesGroup, State


class User(StatesGroup):
    phone = State()
    disease = State()
    disease_type = State()
    age_type2 = State()
    year_type2 = State()
    answer_type2 = State()
    weight_type2 = State()
    height_type2 = State()

    #Bilmayman
    age_type3 = State()
    answer_type3 = State()
    weight_type3 = State()
    height_type3 = State()
    location = State()