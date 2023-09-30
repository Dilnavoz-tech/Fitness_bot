from aiogram.types import ReplyKeyboardMarkup


from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

def mennu_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton("📍 Filial"), KeyboardButton("Start 🏋️‍♂️"))
    markup.add(KeyboardButton("Admin 👨‍🚀"), KeyboardButton("NewsPost"))
    return markup


def menugym_btn():
    menugym = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    menugym.add(KeyboardButton("Woman 👩‍🦰"), KeyboardButton("Man 🤵‍♂️"))
    menugym.add(KeyboardButton("back 🔙"))
    return menugym

def oygym_btn():
    oygym = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    oygym.add(KeyboardButton("1-OY"), KeyboardButton("2-OY"))
    oygym.add(KeyboardButton("3-OY"), KeyboardButton("4-OY"))
    oygym.add(KeyboardButton("Back 🔙"))
    return oygym


def hafta_btn():
    haftagym = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    haftagym.add(KeyboardButton("Dushanba"), KeyboardButton("Seshanba"), KeyboardButton("Chorshanba"))
    haftagym.add(KeyboardButton("Payshanba"), KeyboardButton("Juma"),KeyboardButton("Shanba"))
    haftagym.add(KeyboardButton("Back 🔙"))
    return haftagym


