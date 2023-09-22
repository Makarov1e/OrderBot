
import asyncio
import os
import aiogram.types.input_file
from aiogram import Bot, Dispatcher, F, types
from aiogram.types import Message
from aiogram.filters import Command
import keyboard as kb




bot = Bot(token="6412544139:AAEs_OJXnWcML3gVMjlQ7wX2aIs9MvmzTZ8")
dp = Dispatcher()
num_of_order = input()

@dp.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать! Этот бот способен выводить Вам PDF файл заказа, номер которого Вы указали', reply_markup=kb.main)



@dp.message(F.text == '/document')
async def send_test_file(message: Message):
    for root, dirs, files in os.walk('/users/egormakarov/desktop/test1'):
        flag = False
        for file in files:
            if file == f'{num_of_order}.pdf':
                doc = aiogram.types.input_file.FSInputFile(path=rf'/users/egormakarov/desktop/test1/{file}')
                await bot.send_document(message.chat.id, document=doc)
                flag = True
                break
        if flag == False:
            await message.answer(f'Заказ {num_of_order} не найден...')





@dp.message()
async def echo(message: Message):
    await message.answer('Я тебя не понимаю')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())