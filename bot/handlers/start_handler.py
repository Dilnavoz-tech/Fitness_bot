from datetime import datetime

from aiogram import types

from DB.db import User, session
from bot.buttons.reply import mennu_btn, menugym_btn, oygym_btn, hafta_btn
from bot.dispatcher import dp
from web_main import news_post


@dp.message_handler(lambda message: message.text == "back 🔙")
@dp.message_handler(commands="start")
async def start_hendler(message: types.Message):
    if message.text != "back 🔙":
        now = datetime.now().date()
        user = User(
            chat_id=message.from_user.id,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            username=message.from_user.username,
            join_at=str(now)
        )
        session.add(user)
        session.commit()
        text = """Assalomu alaykum ! 
    Bu bo'timiz sizga kunlik qiladigan 🏋️ mashqlarni ko'rsatib beradi
    """
        await message.bot.send_photo(message.from_user.id, "https://telegra.ph/gym-09-07-2", caption=text,
                                     parse_mode="Markdown", reply_markup=mennu_btn())
    else:
        await message.answer("Kerakli menyuni tanlang ", reply_markup=mennu_btn())


@dp.message_handler(lambda message: message.text == "Admin 👨‍🚀")
async def admin_handler(message: types.Message):
    await message.reply(f"Admin bilan aloqa 📱 "
                        f"https://t.me/Programmist_girl", reply_markup=mennu_btn())


@dp.message_handler(lambda message: message.text == "📍 Filial")
async def filial_hendler(message: types.Message):
    latitude = 41.313605
    longitude = 69.279691
    await message.bot.send_location(message.chat.id, latitude, longitude, reply_markup=mennu_btn())




@dp.message_handler(lambda message: message.text == "Back 🔙")
@dp.message_handler(lambda message: message.text == "Start 🏋️‍♂️")
async def gym_start_hendler(message: types.Message):
    await message.answer("Jinsingizni Tanlang ⤵️", reply_markup=menugym_btn())


@dp.message_handler(lambda message: message.text == "Man 🤵‍♂️")
async def start_hendler(message: types.Message):
    await message.answer("Kerakli oyni tanlang ⬇️", reply_markup=oygym_btn())


@dp.message_handler(lambda message: message.text == "Woman 👩‍🦰")
async def start_hendler(message: types.Message):
    await message.answer("Kerakli oyni tanlang ⬇️", reply_markup=oygym_btn())


@dp.message_handler(lambda message: message.text in ["1-OY", "2-OY", "3-OY", "4-OY"])
async def hafta_hend(message: types.Message):
    await message.answer("Kunni tanlang  ⤵️", reply_markup=hafta_btn())


@dp.message_handler(lambda message: message.text == "NewsPost")
async def start_hendler(message: types.Message):
    for i in news_post():
        text = f"""
    {i.get('title')}
    
    {i.get('text')}
    
    {i.get('time')}"""
        await message.answer_photo(i.get('image'),text, reply_markup=mennu_btn())

