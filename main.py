import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, ReplyKeyboardMarkup
from aiogram.filters import CommandStart
from config import *
import os
import openai

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    kb = [
            [
            types.KeyboardButton(text="Новини"),
            types.KeyboardButton(text="Вчителі"),
            types.KeyboardButton(text="Розклад")
            ],
            [
            types.KeyboardButton(text="Контакти"),
            types.KeyboardButton(text="ШІ-асистент"),
            types.KeyboardButton(text="Адмінпанель")
            ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Оберіть одну з кнопок:"
    )
    await message.answer("Вас вітає Бот-Козак, який завжди готовий прийти на допомогу! Оберіть одну з кнопок, щоб я зміг бути Вам корисним:", reply_markup=keyboard)

@dp.message(F.text.lower() == "повернутися")
async def cmd_start(message: types.Message):
    kb = [
            [
            types.KeyboardButton(text="Новини"),
            types.KeyboardButton(text="Вчителі"),
            types.KeyboardButton(text="Розклад")
            ],
            [
            types.KeyboardButton(text="Контакти"),
            types.KeyboardButton(text="ШІ-асистент"),
            types.KeyboardButton(text="Адмінпанель")
            ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Оберіть одну з кнопок:"
    )
    await message.answer("Вас вітає Бот-Козак, який завжди готовий прийти на допомогу! Оберіть одну з кнопок, щоб я зміг бути Вам корисним:", reply_markup=keyboard)

@dp.message(F.text.lower() == "новини")
async def news(message: types.Message):
    await message.reply("У нас є гарні новини! Перейдіть за посиланням, щоб побачити свіжу інформацію: http://inter4.zp.ua/news\nТакож завітайте до наших соц-мереж:\nInstagram: https://www.instagram.com/zp.cossack_lyceum/\nFacebook: https://www.facebook.com/profile.php?id=100094544324104&locale=uk_UA")

@dp.message(F.text.lower() == "вчителі")
async def teachers(message: types.Message):
    await message.reply("Вчителі завжди готові вам допомогти! Ось педагоги нашої школи: http://inter4.zp.ua/teacher/view_one/?parent_id=2")

@dp.message(F.text.lower() == "розклад")
async def schedule(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="5"),
            types.KeyboardButton(text="6"),
            types.KeyboardButton(text="7")
        ],
        [
            types.KeyboardButton(text="8"),
            types.KeyboardButton(text="9"),
            types.KeyboardButton(text="10")
        ],
        [
            types.KeyboardButton(text="11"),
            types.KeyboardButton(text="Повернутися")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Оберіть свій клас:"
    )
    await message.answer("Оберіть свій клас:", reply_markup=keyboard)

@dp.message(F.text.lower() == "5")
async def five(message: types.Message):
    await message.reply("Ось розклад всієї паралелі, тут є і Ваш: https://drive.google.com/drive/folders/1qZ5_szCdQgAuJ_8ufhK9h6B3Ub2_WAdN?usp=sharing")

@dp.message(F.text.lower() == "6")
async def six(message: types.Message):
    await message.reply("Ось розклад всієї паралелі, тут є і Ваш: https://drive.google.com/drive/folders/1qZ5_szCdQgAuJ_8ufhK9h6B3Ub2_WAdN?usp=sharing")

@dp.message(F.text.lower() == "7")
async def seven(message: types.Message):
    await message.reply("Ось розклад всієї паралелі, тут є і Ваш: https://drive.google.com/drive/folders/1qZ5_szCdQgAuJ_8ufhK9h6B3Ub2_WAdN?usp=sharing")
@dp.message(F.text.lower() == "8")
async def eight(message: types.Message):
    await message.reply("Ось розклад всієї паралелі, тут є і Ваш: https://drive.google.com/drive/folders/1qZ5_szCdQgAuJ_8ufhK9h6B3Ub2_WAdN?usp=sharing")

@dp.message(F.text.lower() == "9")
async def nine(message: types.Message):
    await message.reply("Ось розклад всієї паралелі, тут є і Ваш: https://drive.google.com/drive/folders/1qZ5_szCdQgAuJ_8ufhK9h6B3Ub2_WAdN?usp=sharing")

@dp.message(F.text.lower() == "10")
async def ten(message: types.Message):
    await message.reply("Ось розклад всієї паралелі, тут є і Ваш: https://drive.google.com/drive/folders/1qZ5_szCdQgAuJ_8ufhK9h6B3Ub2_WAdN?usp=sharing")

@dp.message(F.text.lower() == "11")
async def eleven(message: types.Message):
    await message.reply("Ось розклад всієї паралелі, тут є і Ваш: https://drive.google.com/drive/folders/1qZ5_szCdQgAuJ_8ufhK9h6B3Ub2_WAdN?usp=sharing")

@dp.message(F.text.lower() == "контакти")
async def contacts(message: types.Message):
    await message.reply("Контакти:\nНазва закладу: Комунальний заклад 'Запорізька спеціалізована школа-інтернат ІІ-ІІІ ступенів 'Козацький ліцей'' Запорізької обласної ради\nСкорочена назва: Запорізька школа-інтернат 'Козацький ліцей'\nАдреса: 69065, Запоріжжя, Дніпровський район, вул. Щаслива, 2\nТелефон/факс: +38 (061) 224-79-67\nЕ-mail: zp.inter4@ukr.net")

@dp.message(F.text.lower() == "ші-асистент")
async def ai(message: types.Message):
    await message.reply("Ось посилання на бета-версію бота з ші, скоро він з'явиться і у цьому чаті: https://t.me/aiii_test_bot")

@dp.message(F.text.lower() == "адмінпанель")
async def admin(message: types.Message):
    await message.reply("Скоро для адміністраторів з'явиться можливість додавати оголошення для інших користувачів, очікуйте на оновлення!")

@dp.message()
async def message_handler(message: types.Message):
    answer = await ai(message.text)
    if answer != None:
        await message.reply(answer)
    else:
        await message.reply("Виникла помилка, спробуйте ще раз.")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())