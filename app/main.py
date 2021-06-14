from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from user_commands import *
import asyncio
from config import TOKEN
from lists import *
import random

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

message_count = 1


async def writeToLogs(message: types.Message):
    global message_count
    obj = str(message_count) + ": " + str(message) + '\n'
    file = open('logs.txt', 'a')
    file.write(obj)
    message_count += 1


async def printMessageDate(message: types.Message):
    print("User request:")

    print('|\tUserInfo:', message.from_user)
    print("|\tChatInfo:", message.chat)
    print("|\tMessageType:", message.content_type)
    print("|\tDate:", message.date)
    print('\n')


@dp.message_handler(content_types=types.ContentType.TEXT)
async def process_start_command(message: types.Message):
    current_user = str(message.from_user.username)

    if current_user == 'Brigory':
        await message.reply('ЛЯХ ЛОСЬ!')


@dp.message_handler(commands=['test'])
async def process_start_command(message: types.Message):
    if str(message.text) == '/test huy':
        await message.reply('Повідомлення буде видалено через 5 секунд')
        await asyncio.sleep(5)
        await message.chat.delete_message(message.message_id)


if __name__ == '__main__':
    executor.start_polling(dp)
