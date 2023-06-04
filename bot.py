from aiogram import Bot, Dispatcher, types, executor

TOKEN = '6198687861:AAHXYEh4DacXEdslG_NFfVjan_fQHTs8HuE'

import string
import random

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['description'])
async def decs_command(message: types.Message):
    await message.answer('Данный бот умеет отправлять рандомные символы латинского алфавита')
    await message.delete()

@dp.message_handler(commands=['count'])
async def check_count(message: types.Message):
    global count
    await message.answer(f'COUNT: {count}')
    count += 1


@dp.message_handler()
async def send_check_zero(message: types.Message):
    if '0' in message.text:
    
        await message.reply('YES')
    else:
        await message.reply('NO')
    

@dp.message_handler()
async def send_random_letter(message: types.Message):
    await message.reply(random.choice(string.ascii_letters))



if __name__ == '__main__':
    executor.start_polling(dp)
