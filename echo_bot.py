from aiogram import Dispatcher, Bot, executor, types
from dotenv import load_dotenv
import os
import logging

load_dotenv()
telegram_token = os.environ.get('TELEGRAM_API_TOKEN')

bot = Bot(token=telegram_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def command_start_handler(message: types.Message):
    await message.reply('Hi! \n Im an echo_bot powered by aiogram')

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)