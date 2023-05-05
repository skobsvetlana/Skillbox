import logging

from aiogram import Router, F, html, Bot
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.utils.markdown import text, bold

from tgbot.keyboards.simple_row import make_row_keyboard
from tgbot.logger import log

from data_collection.high import high

from typing import Any, Dict

currency_router = Router()

available_cmd = ["CURRENCY", "HISTORY", "HELP"]
available_currency = ["BTC", "ETH"]
available_currency_cmd = ["LOW", "HIGH", "CUSTOM"]

class Currency(StatesGroup):
    start_state: State = State()
    common_cmd_state: State = State()
    currency_state: State = State()
    currency_cmd_state = State()
    custom_state = State()


@currency_router.message(Command("start"))
async def command_start(message: Message, state: FSMContext) -> None:
    await state.set_state(Currency.start_state)
    await message.answer(
        f"Привет!\nЯ могу показать минимальный/максимальный "
        f"курс выбранной криптовалюты в usdt\nза предыдущий день или за выбранный период.")
    await message.answer(
        f"Могу показать историю выполненных тобою команд ")
    await message.answer(f"Используй /help, чтобы узнать список доступных команд!",
                         reply_markup=make_row_keyboard(available_cmd))
    await state.set_state(Currency.common_cmd_state)


@currency_router.message(Command("help"))
async def process_help_command(message: Message):
    log(message)
    msg = text(bold('Я могу ответить на следующие команды:'),
               '/low', '/high', '/custom', '/history','/currency', sep='\n')
    await message.answer(msg)


@currency_router.message(Command("cancel"))
@currency_router.message(F.text.casefold() == "cancel")
async def cancel_handler(message: Message, state: FSMContext) -> None:
    """
    Allow user to cancel any action
    """
    log(message)
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info("Cancelling state %r", current_state)
    await state.clear()
    await message.answer(
        "Cancelled.",
        reply_markup=ReplyKeyboardRemove(),
    )


@currency_router.message(Currency.common_cmd_state, F.text.casefold() == "currency")
async def process_currency(message: Message, state: FSMContext) -> None:
    log(message)
    await state.set_state(Currency.currency_state)
    data = await state.update_data(common_cmd=message.text)
    await message.answer(
        "Отлично!\nВыбери криптовалюту",
        reply_markup=make_row_keyboard(available_currency),
    )


@currency_router.message(Currency.common_cmd_state, F.text.casefold() == "history")
async def process_history(message: Message, state: FSMContext) -> None:
    log(message)
    data = await state.get_data()
    print(data)
    await state.clear()
    await message.answer(
        "Вот история выполненных команд.",
        reply_markup=ReplyKeyboardRemove(),
    )
    await state.clear()
    await state.set_state(Currency.common_cmd_state)
    await message.answer(f"Начинаем сначала", reply_markup=make_row_keyboard(available_cmd))
    #await show_summary(message=message, data=data, positive=False)


@currency_router.message(Currency.common_cmd_state, F.text.casefold() == "help")
async def process_help(message: Message, state: FSMContext) -> None:
    log(message)
    data = await state.get_data()
    await state.clear()
    msg = text(bold('Я могу ответить на следующие команды:'),
               '/low', '/high', '/custom', '/history', '/currency', sep='\n')
    await message.reply(msg,reply_markup=ReplyKeyboardRemove(),)
    await state.clear()
    await state.set_state(Currency.common_cmd_state)
    await message.answer(f"Начинаем сначала. Выбери команду.", reply_markup=make_row_keyboard(available_cmd))
    #await show_summary(message=message, data=data, positive=False)


@currency_router.message(Currency.common_cmd_state)
async def process_unknown_message(message: Message, state: FSMContext) -> None:
    log(message)
    await message.reply("Я не понимаю тебя. Попробуй еще раз.")


@currency_router.message(Currency.currency_state, F.text.casefold() == "eth")
@currency_router.message(Currency.currency_state, F.text.casefold() == "btc")
async def process_currency_cmd(message: Message, state: FSMContext) -> None:
    log(message)
    await state.set_state(Currency.currency_cmd_state)
    data = await state.update_data(currency=message.text)
    await message.answer(
        "Отлично!\nВыбери команду",
        reply_markup=make_row_keyboard(available_currency_cmd),
    )


@currency_router.message(Currency.currency_cmd_state, F.text.casefold() == "low")
async def process_low_cmd(message: Message, state: FSMContext) -> None:
    log(message)
    data = await state.update_data(cmd=message.text)
    print(data)
    text = "Ты выбрал LOW."

    await state.clear()
    await message.answer(text)
    await state.set_state(Currency.common_cmd_state)
    await message.answer(f"Начинаем сначала. Выбери команду", reply_markup=make_row_keyboard(available_cmd))
    # await show_summary(message=message, data=data)


@currency_router.message(Currency.currency_cmd_state, F.text.casefold() == "high")
async def process_high_cmd(message: Message, state: FSMContext) -> None:
    log(message)
    data = await state.update_data(cmd=message.text)
    print(data)
    text = "Ты выбрал HIGH."

    await state.clear()
    await message.answer(text)
    await state.set_state(Currency.common_cmd_state)
    await message.answer(f"Начинаем сначала. Выбери команду.", reply_markup=make_row_keyboard(available_cmd))
    # await show_summary(message=message, data=data)


@currency_router.message(Currency.currency_cmd_state, F.text.casefold() == "custom")
async def process_custom(message: Message, state: FSMContext) -> None:
    await state.set_state(Currency.custom_state)
    log(message)
    await message.answer("Введи диапазон в днях", reply_markup=ReplyKeyboardRemove(), )
    data = await state.get_data()


@currency_router.message(Currency.custom_state)
async def process_chosing_custom(message: Message, state: FSMContext) -> None:
    log(message)
    data = await state.update_data(scope=message.text)

    await state.set_state(Currency.currency_cmd_state)
    await message.answer(
        "Отлично!\nВыбери команду",
        reply_markup=make_row_keyboard(available_currency_cmd),
    )
    # await show_summary(message=message, data=data)


async def show_summary(message: Message, data: Dict[str, Any], positive: bool = True) -> None:
    name = data["name"]
    currency = data.get("currency", "<something unexpected>")
    text = f"I'll keep in mind that, {html.quote(name)}, "
    text += (
        f"you like to write bots with {html.quote(currency)}."
        if positive
        else "you don't like to write bots, so sad..."
    )
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())


