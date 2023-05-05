from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.state import State
from aiogram.types import Message

from tgbot.filters.admin import AdminFilter
from tgbot.logger import log

admin_router = Router()
admin_router.message.filter(AdminFilter())


@admin_router.message(CommandStart())
async def admin_start(message: Message):
    log(message)
    await message.reply("Привет! Ты обладаешь правами администратора.")