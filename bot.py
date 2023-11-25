# bot.py

import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from parser import get_latest_news
from config import NEWS_URLS

API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    if message.text.lower() == '/start':
        return  # игнорируем команду /start
    await message.reply("Привет! Я бот с курсами, шаблонами и новостями. Используйте команды /courses, /templates и /news.")


@dp.message_handler(commands=['courses'])
async def send_courses(message: types.Message):
    # Ваш код для обработки команды /courses
    await message.reply("Вот доступные курсы:")


@dp.message_handler(commands=['templates'])
async def send_templates(message: types.Message):
    # Ваш код для обработки команды /templates
    await message.reply("Вот доступные шаблоны:")


@dp.message_handler(commands=['news'])
async def send_news(message: types.Message):
    await message.reply("Идет поиск свежих новостей.")
    latest_news = get_latest_news(NEWS_URLS)

    if latest_news:
        news_text = "\n".join(latest_news)
        await bot.send_message(message.chat.id, f"Вот последние новости:\n{news_text}", parse_mode=ParseMode.MARKDOWN)
    else:
        await bot.send_message(message.chat.id, "Извините, не удалось получить новости.")


if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
