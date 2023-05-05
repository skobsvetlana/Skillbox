from tgbot.logger import log

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    log(message)
    await message.reply("Привет!")


# @dp.message_handler(commands=['hi6'])
# async def process_hi6_command(message: types.Message):
#     await message.reply("Шестое - запрашиваем контакт и геолокацию\nЭти две кнопки не зависят друг от друга",
#                         reply_markup=keyboards.markup_request)


# @dp.message_handler(commands='ссылки')
# async def url_command(message: types.Message):
#     await message.answer('Полезные ссылки:', reply_markup=urlkb)





