import asyncio
import logging
import betterlogging as bl

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.strategy import FSMStrategy

from tgbot.config import config
from tgbot.handlers import currency

logger = logging.getLogger(__name__)
log_level = logging.INFO
bl.basic_colorized_config(level=log_level)

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(config.bot_token.get_secret_value())
    dp.include_routers(currency.currency_router)

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    #logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())





# # Хэндлер на команду /start
# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     await message.answer("Hello!")
#
# # Хэндлер на команду /test1
# @dp.message(Command("test1"))
# async def cmd_test1(message: types.Message):
#     await message.reply("Test 1")
#
# # Хэндлер на команду /test2
# async def cmd_test2(message: types.Message):
#     await message.reply("Test 2")
#
#
# @dp.message(Command("answer"))
# async def cmd_answer(message: types.Message):
#     await message.answer("Это простой ответ")
#
#
# @dp.message(Command("reply"))
# async def cmd_reply(message: types.Message):
#     await message.reply('Это ответ с "ответом"')
#
#
# @dp.message(Command("add_to_list"))
# async def cmd_add_to_list(message: types.Message, mylist: list[int]):
#     mylist.append(7)
#     await message.answer("Добавлено число 7")
#
#
# @dp.message(Command("show_list"))
# async def cmd_show_list(message: types.Message, mylist: list[int]):
#     await message.answer(f"Ваш список: {mylist}")
#
#
# # Запуск процесса поллинга новых апдейтов
# async def main():
#     # Где-то в другом месте, например, в функции main():
#     dp.message.register(cmd_test2, Command("test2"))
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())








