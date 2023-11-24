from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot_token

import logging
import os
import random

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

STORAGE_PATH = "storage"  # Путь к папке с файлами

logging.basicConfig(level=logging.INFO)

bot = Bot(token=bot_token)
dp = Dispatcher(bot)

BUTTON_RUSSIAN = "button1"
BUTTON_ENGLISH = "button2"
BUTTON_MENU = "menu"
BUTTON_TEMPLATES = "button3"
BUTTON_COURSES = "button4"

ranmess = ''

TEXT_SET_LANGUAGE = "Set the language:"
TEXT_CHOSE_RUSSIAN = "Выберите язык:"
TEXT_IN_PROGRESS = "In progress."


def get_inline_keyboard_to_start():
    keyboard_start = InlineKeyboardMarkup(row_width=2)
    button1 = InlineKeyboardButton(text="Русский", callback_data=BUTTON_RUSSIAN)
    button2 = InlineKeyboardButton(text="English", callback_data=BUTTON_ENGLISH)
    keyboard_start.add(button1, button2)
    return keyboard_start

def get_inline_keyboard_for_menu():
    keyboard_menu = InlineKeyboardMarkup()
    menu_button = InlineKeyboardButton(text="Menu", callback_data=BUTTON_MENU)
    keyboard_menu.add(menu_button)
    return keyboard_menu

def get_inline_keyboard_to_main():
    keyboard_main = InlineKeyboardMarkup(row_width=2)
    button3 = InlineKeyboardButton(text="Шаблоны", callback_data=BUTTON_TEMPLATES)
    button4 = InlineKeyboardButton(text="Курсы", callback_data=BUTTON_COURSES)
    keyboard_main.add(button3, button4)
    return keyboard_main

@dp.message_handler(Command("start"))
async def send_welcome(message: types.Message):
    keyboard = get_inline_keyboard_to_start()
    await bot.send_message(message.chat.id, TEXT_SET_LANGUAGE, reply_markup=keyboard)

async def send_keyboard_message(chat_id, text, buttons):
    keyboard = InlineKeyboardMarkup()
    for btn_text, btn_callback in buttons:
        button = InlineKeyboardButton(text=btn_text, callback_data=btn_callback)
        keyboard.add(button)
    await bot.send_message(chat_id, text, reply_markup=keyboard)

async def send_file(chat_id, file_path, caption):
    with open(file_path, "rb") as file:
        await bot.send_document(chat_id, file, caption=caption)

@dp.callback_query_handler(lambda c: c.data in [BUTTON_RUSSIAN, BUTTON_ENGLISH, BUTTON_MENU, BUTTON_TEMPLATES, BUTTON_COURSES, "template1", "template2", "course1", "course2"])
async def process_callback_button(callback_query: types.CallbackQuery):
    logging.info(f"Received callback query: {callback_query}")
    await bot.answer_callback_query(callback_query.id)
    button_data = callback_query.data

    if button_data == BUTTON_RUSSIAN:
        buttons = [("Шаблоны", BUTTON_TEMPLATES), ("Курсы", BUTTON_COURSES)]
        await send_keyboard_message(callback_query.from_user.id, TEXT_CHOSE_RUSSIAN, buttons)
    elif button_data == BUTTON_ENGLISH:
        buttons = [("Menu", BUTTON_MENU)]
        await send_keyboard_message(callback_query.from_user.id, TEXT_IN_PROGRESS, buttons)
    elif button_data == BUTTON_MENU:
        buttons = [("Русский", BUTTON_RUSSIAN), ("English", BUTTON_ENGLISH)]
        await send_keyboard_message(callback_query.from_user.id, TEXT_SET_LANGUAGE, buttons)
    elif button_data == BUTTON_TEMPLATES:
        logging.info("Pressed Templates button")
        template_buttons = [
            ("Шаблон 1", "template1"),
            ("Шаблон 2", "template2")
        ]
        await send_keyboard_message(callback_query.from_user.id, "Выберите шаблон:", template_buttons)
    elif button_data == BUTTON_COURSES:
        course_buttons = [
            ("Курс 1", "course1"),
            ("Курс 2", "course2")
        ]
        await send_keyboard_message(callback_query.from_user.id, "Выберите курс:", course_buttons)
    elif button_data == "template1":
        logging.info("Pressed Template 1 button")
        file_path = os.path.join(STORAGE_PATH, "template1.zip")
        caption = "Файл: template1.zip"
        logging.info(f"File path: {file_path}")
        try:
            await send_file(callback_query.from_user.id, file_path, caption)
        except Exception as e:
            logging.error(f"Error sending file: {e}")
    elif button_data == "template2":
        logging.info("Pressed Template 2 button")
        file_path = os.path.join(STORAGE_PATH, "template2.zip")
        caption = "Файл: template2.zip"
        logging.info(f"File path: {file_path}")
        try:
            await send_file(callback_query.from_user.id, file_path, caption)
        except Exception as e:
            logging.error(f"Error sending file: {e}")
    elif button_data == "course1":
        logging.info("Pressed Course 1 button")
        file_path = os.path.join(STORAGE_PATH, "course1.zip")
        caption = "Файл: course1.zip"
        logging.info(f"File path: {file_path}")
        try:
            await send_file(callback_query.from_user.id, file_path, caption)
        except Exception as e:
            logging.error(f"Error sending file: {e}")
    elif button_data == "course2":
        logging.info("Pressed Course 2 button")
        file_path = os.path.join(STORAGE_PATH, "course2.zip")
        caption = "Файл: course2.zip"
        logging.info(f"File path: {file_path}")
        try:
            await send_file(callback_query.from_user.id, file_path, caption)
        except Exception as e:
            logging.error(f"Error sending file: {e}")
@dp.message_handler()
async def handle_text(message: types.Message):
    # Обработка текстовых сообщений
    if message.text == 'Курс 1':
        # Логика для отправки файла курса 1
        pass
    elif message.text == 'Курс 2':
        # Логика для отправки файла курса 2
        pass
    elif message.text == 'Шаблон 1':
        # Логика для отправки файла шаблона 1
        pass
    elif message.text == 'Шаблон 2':
        # Логика для отправки файла шаблона 2
        pass
    else:
        # Если текст не соответствует ожидаемым командам
        # Генерация случайного числа от 1 до 5
        rannum = random.randint(1, 5)
        if rannum == 1:
            ranmess = 'Я вас не понял. Напишите команду'
        elif rannum == 2:
            ranmess = 'Не понимаю вас. Напишите команду'
        elif rannum == 3:
            ranmess = 'Что вы имели ввиду? Напишите команду'
        elif rannum == 4:
            ranmess = 'Я не знаю такой команды. Напишите команду'
        else:
            ranmess = 'Что это значит? Напишите команду'
        await bot.send_message(message.chat.id, ranmess)

if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
