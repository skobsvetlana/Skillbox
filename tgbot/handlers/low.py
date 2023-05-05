from aiogram import types
from aiogram import Router

from tgbot.logger import log
from data_collection.low import low

from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.markdown import text, bold


router = Router()

@router.message(Command("low"))
async def process_low_command(message: types.Message):
    log(message)
    # await message.reply("Выбери криптовалюту курс которой ты хочешь увидеть.",
    #                     reply_markup=keyboards.markup_currency_choice)
    await message.reply("LOW", reply_markup=keyboards.inline_kb_low)

@router.callback_query(lambda c: c.data == 'LOW')
async def process_callback_button_low(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)  # Отправляем подтверждение обработки callback запроса
    await bot.send_message(callback_query.from_user.id, (low()))  # Вызываем вашу функцию