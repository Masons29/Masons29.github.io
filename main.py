import os
import logging
import random
import asyncio
import timeit
import aiogram
from aiogram.utils.deep_linking import get_start_link, decode_payload
from re import search
from aiogram import Bot, Dispatcher, executor, types, filters
import users
from time import sleep
from datetime import datetime
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import json
import urllib
from io import BytesIO
from PIL import Image
API_TOKEN="5927701926:AAGmbx-su6N5uXbowsZJXkFjE08P4Ci9sQ0"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

#Создание базы данных
users.CreateDB()
button1 = InlineKeyboardButton(text="Принять✅", callback_data="button1")
buttonn1 = InlineKeyboardMarkup().add(button1)
nk2 = InlineKeyboardMarkup(row_width=1)
nk2.add(button1)


@dp.message_handler(commands='start')
async def test(message):
    #Вытаскиваем с базы
    users.cursor.execute(f"SELECT * FROM users where id = {message.from_user.id}")
    #Проверяем есть ли пользователь в базе
    if users.cursor.fetchone() == None:
        #Сохраняем если нету
        users.InsertValue(message.from_user.first_name, message.from_user.id)
    #Рандомим выигрыш
        await message.reply("Вы принимаете всю ответственность за совершенные действия",reply_markup=nk2)
    #Сохраняем в базу
    #Отключаемся от базы
        users.con.commit()
    else:
            await message.reply(f'✅ Вы уже зарегистрированы!\n\n/info - посмотреть свой профиль', parse_mode='html')

    

@dp.callback_query_handler(lambda c: c.data == "button1")
async def callback_mason_n(callback_query: types.CallbackQuery):
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        await bot.send_message(callback_query.message.chat.id, f"""Вы успешно приняли ответственность ✅\n\nИ приветствуем вас в нашем магазине Mason shop, здесь вы можете приобрести товары как 'Доксы, Сносы телеграмм каналов, Спортиков, Мануалы'\n\n/info - посмотреть свой профиль""")

photo = 'AgACAgIAAxkBAAEBlnpjuZDjL7B_zoKQ4mPL3_M0ZMKfnQAC0cIxG6fDyEmHmDVP7rVLAAEBAAMCAANzAAMtBA'

button5 = InlineKeyboardButton(text="Товары 🛍️", callback_data="button5")
button6 = InlineKeyboardButton(text="Тех.поддержка ⚠️", callback_data="button6")
buttonn2 = InlineKeyboardMarkup().add(button5, button6)
n2 = InlineKeyboardMarkup(row_width=1)
n2.add(button5, button6)

@dp.callback_query_handler(lambda c: c.data == "button6")
async def callback_mason_n(callback_query: types.CallbackQuery):
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        await bot.send_message(callback_query.message.chat.id, f"""Нашли ошибку? или не пришел товар? пишите Администрации Бота: @Masons_family\n""")



@dp.message_handler(commands=['инфа', 'инф', 'инфо', 'info', 'стата'], commands_prefix='!./')
async def information(message: types.Message):
    username = message.from_user.username
    balance = users.cursor.execute("SELECT balance from users where id = ?", (message.from_user.id,)).fetchone()
    balance = (balance[0])
    id = message.from_user.id
    name = users.cursor.execute("SELECT name from users where id = ?", (message.from_user.id,)).fetchone()
    name = (name[0])
    await bot.send_message(message.chat.id,f"""
<b>Имя пользователя:</b> {name}
<b>Id пользователя:</b> {id}


<b>👤 Юзернейм:</b> @{username} 
<b>💰 Баланс</b>: {balance}""",parse_mode = "html", reply_markup=n2)

button7 = InlineKeyboardButton(text="Докс", callback_data="button7")
button8 = InlineKeyboardButton(text="Сват",callback_data="button8")
button9 = InlineKeyboardButton(text="Взлом Вк и Инстаграмма", callback_data="button9")
button10 = InlineKeyboardButton(text="Ддос", callback_data="button10")
button11 = InlineKeyboardButton(text="Спортики", callback_data="button11")
button12 = InlineKeyboardButton(text="Снос телеграмм каналов, групп", callback_data="button12")
button13 = InlineKeyboardButton(text="Снос телеграмм аккаунтов", callback_data="button13")

buttonn2 = InlineKeyboardMarkup().add(button7, button8, button9, button10, button11, button12, button13)
n = InlineKeyboardMarkup(row_width=1)
n.add(button7, button8, button9, button10, button11, button12, button13)



@dp.callback_query_handler(lambda c: c.data == "button5")
async def callback_mason_n(callback_query: types.CallbackQuery):
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        await bot.send_message(callback_query.message.chat.id, f"""Все доступные товары вы можете увидеть ниже""", reply_markup=n)

@dp.callback_query_handler(lambda c: c.data == "button7")
async def callback_mason_n(callback_query: types.CallbackQuery):
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        await bot.send_message(callback_query.message.chat.id, f"""Номер заказа: 7\n\n1.Докс - начинающий = 100 Рублей\nСредний = 250 Рублей\nЛучший = 500 Рублей\n\nqiwi.com/p/79670068632 - что бы заказать товар, кидайте деньги на киви с комментарием <номер заказа>""")

@dp.callback_query_handler(lambda c: c.data == "button8")
async def callback_mason_n(callback_query: types.CallbackQuery):
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        await bot.send_message(callback_query.message.chat.id, f"""Номер заказа: 8\n\nСват [ минирование] 600 рублей\nПохоронное бюро= 300 рублей\nМчс = 100 рублей\nЭвакуация вашего здания = 700 рублей\n\nqiwi.com/p/79670068632 - что бы заказать товар, кидайте деньги на киви с комментарием <номер заказа> """)

@dp.callback_query_handler(lambda c: c.data == "button9")
async def callback_mason_n(callback_query: types.CallbackQuery):
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        await bot.send_message(callback_query.message.chat.id, f"""Номер заказа: 9\n\nВзлом вк , инстаграм:\nВк = 1000 рублей\nИнстаграм= 1300\n\nqiwi.com/p/79670068632 - что бы заказать товар, кидайте деньги на киви с комментарием <номер заказа>""")


@dp.callback_query_handler(lambda c: c.data == "button10")
async def callback_mason_n(callback_query: types.CallbackQuery):
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        await bot.send_message(callback_query.message.chat.id, f"""Номер заказа: 10\n\nДдос - слабый = 250 рублей\nСредний = 400\nМощный = 1000\n\nqiwi.com/p/79670068632 - что бы заказать товар, кидайте деньги на киви с комментарием <номер заказа>""")

@dp.callback_query_handler(lambda c: c.data == "button11")
async def callback_mason_n(callback_query: types.CallbackQuery):
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        await bot.send_message(callback_query.message.chat.id, f"""Номер заказа: 11\n\nСпортики = 1300 Рублей\n\nqiwi.com/p/79670068632 - что бы заказать товар, кидайте деньги на киви с комментарием <номер заказа>""")

  

@dp.callback_query_handler(lambda c: c.data == "button12")
async def callback_mason_r(callback_query: types.CallbackQuery):
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        await bot.send_message(callback_query.message.chat.id, f"""Номер заказа: 12\n\nСнос телеграм акаунтов и каналов = 600 Рублей\n\nqiwi.com/p/79670068632 - что бы заказать товар, кидайте деньги на киви с комментарием <номер заказа>""")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)