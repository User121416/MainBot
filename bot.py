from config import bot_token
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token=bot_token)
dp = Dispatcher(bot)

def get_inline_keyboard_to_start():
    keyboard_start = InlineKeyboardMarkup(row_width=2)
    button1 = InlineKeyboardButton(text="Русский", callback_data="button1")
    button2 = InlineKeyboardButton(text="English", callback_data="button2")
    keyboard_start.add(button1, button2)
    return keyboard_start

def get_inline_keyboard_for_menu():
    keyboard_menu = InlineKeyboardMarkup()
    menu_button = InlineKeyboardButton(text="Menu", callback_data="menu")
    keyboard_menu.add(menu_button)
    return keyboard_menu

def get_inline_keyboard_to_main():
    keyboard_main = InlineKeyboardMarkup(row_width=2)
    button3 = InlineKeyboardButton(text="Шаблоны", callback_data="button3")
    button4 = InlineKeyboardButton(text="Курсы", callback_data="button4")
    keyboard_main.add(button3, button4)
    return keyboard_main

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = get_inline_keyboard_to_start()
    await bot.send_message(message.chat.id, "Set the language:", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data in ['button1', 'button2', 'menu', 'button3', 'button4'])
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    button_data = callback_query.data

    if button_data == 'button1':
        keyboard_main = get_inline_keyboard_to_main()
        await bot.send_message(callback_query.from_user.id, 'Вы выбрали Русский.', reply_markup=keyboard_main)
    elif button_data == 'button2':
        keyboard_menu = get_inline_keyboard_for_menu()
        await bot.send_message(callback_query.from_user.id, 'In progress.', reply_markup=keyboard_menu)
    elif button_data == 'menu':
        keyboard_start = get_inline_keyboard_to_start()
        await bot.send_message(callback_query.from_user.id, "Set the language:", reply_markup=keyboard_start)
    # Добавьте обработку для button3 и button4 при необходимости

@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)