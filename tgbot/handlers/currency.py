import logging

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.utils.markdown import text, bold

from tgbot.keyboards.simple_row import make_row_keyboard
from tgbot.logger import log
from tgbot.messages import MESSAGES
from tgbot.history import get_history

from data_collection.high import high
from data_collection.low import low

from typing import Any, Dict

currency_router = Router()

available_cmd = ["CURRENCY", "HISTORY", "HELP"]
available_currency = ["BTC", "ETH", "CANCEL"]
available_range_cmd = ["LAST DAY", "CUSTOM", "CANCEL"]
available_currency_cmd = ["LOW", "HIGH", "CANCEL"]

class Currency(StatesGroup):
    start_state: State = State()
    common_cmd_state: State = State()
    currency_state: State = State()
    currency_cmd_state = State()
    custom_state = State()
    last_day_state = State()


@currency_router.message(Command("start"))
async def command_start(message: Message, state: FSMContext) -> None:
    await state.set_state(Currency.start_state)
    await message.answer(MESSAGES['start'], reply_markup=make_row_keyboard(available_cmd))
    await state.set_state(Currency.common_cmd_state)


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
    await state.set_state(Currency.common_cmd_state)
    await message.answer(f"Выбери команду.", reply_markup=make_row_keyboard(available_cmd))
    

@currency_router.message(Command("currency"))
@currency_router.message(Currency.common_cmd_state, F.text.casefold() == "currency")
async def process_currency(message: Message, state: FSMContext) -> None:
    log(message)
    await state.set_state(Currency.currency_state)
    await state.update_data(common_cmd=message.text)
    await message.answer(
        "Отлично!\nВыбери криптовалюту.",
        reply_markup=make_row_keyboard(available_currency),
    )

@currency_router.message(Command("history"))
@currency_router.message(Currency.common_cmd_state, F.text.casefold() == "history")
async def process_history(message: Message, state: FSMContext) -> None:
    log(message)
    user_id = message.from_user.id
    user_history = get_history(str(user_id))
    for el in user_history:
        await message.answer(text=str(el))
    await state.clear()
    await state.set_state(Currency.common_cmd_state)
    await message.answer(f"Выбери команду.", reply_markup=make_row_keyboard(available_cmd))


@currency_router.message(Command("help"))
@currency_router.message(Currency.common_cmd_state, F.text.casefold() == "help")
async def process_help_command(message: Message, state: FSMContext) -> None:
    log(message)
    await state.clear()
    msg = text(bold('Я могу ответить на следующие команды:'), '\n',
               MESSAGES['low'], MESSAGES['high'],
               MESSAGES['last_day'], MESSAGES['custom'],
               MESSAGES['currency'], MESSAGES['history'], sep='\n')
    await message.answer(msg, reply_markup=ReplyKeyboardRemove(),)
    await state.set_state(Currency.common_cmd_state)
    await message.answer(f"Выбери команду.", reply_markup=make_row_keyboard(available_cmd))



@currency_router.message(Currency.common_cmd_state)
async def process_unknown_message(message: Message, state: FSMContext) -> None:
    log(message)
    await message.reply("Я не понимаю тебя. Попробуй еще раз.", reply_markup=ReplyKeyboardRemove(),)
    await state.set_state(Currency.common_cmd_state)
    await message.answer(f"Выбери команду.", reply_markup=make_row_keyboard(available_cmd))


@currency_router.message(Currency.currency_state, F.text.casefold() == "eth")
@currency_router.message(Currency.currency_state, F.text.casefold() == "btc")
async def process_currency_cmd(message: Message, state: FSMContext) -> None:
    log(message)
    await state.set_state(Currency.currency_cmd_state)
    await state.update_data(currency=message.text)
    await message.answer("Отлично!\nВыбери период")
    await message.answer(
        "Нажми LAST DAY, если хочешь получить информацию за последний прошедший день.\n"
        "Нажми CUSTOM, если хочешь выбрать интервал. Максимальный интервал - 2000 дней.",
        reply_markup=make_row_keyboard(available_range_cmd),
    )


@currency_router.message(Command("low"))
@currency_router.message(Currency.currency_cmd_state, F.text.casefold() == "low")
async def process_low_cmd(message: Message, state: FSMContext) -> None:
    log(message)
    data = await state.update_data(currency_cmd=message.text.lower())
    await state.clear()
    await state.set_state(Currency.common_cmd_state)
    await show_result(message=message, data=data)
    await message.answer(f"Выбери команду.", reply_markup=make_row_keyboard(available_cmd))


@currency_router.message(Command("high"))
@currency_router.message(Currency.currency_cmd_state, F.text.casefold() == "high")
async def process_high_cmd(message: Message, state: FSMContext) -> None:
    log(message)
    data = await state.update_data(currency_cmd=message.text.lower())
    await state.clear()
    await state.set_state(Currency.common_cmd_state)
    await show_result(message=message, data=data)
    await message.answer(f"Выбери команду.", reply_markup=make_row_keyboard(available_cmd))

@currency_router.message(Command("last_day"))
@currency_router.message(Currency.currency_cmd_state, F.text.casefold() == "last day")
async def process_custom(message: Message, state: FSMContext) -> None:
    await state.set_state(Currency.last_day_state)
    log(message)
    await state.update_data(my_range=1)
    #data = await state.get_data()
    await state.set_state(Currency.currency_cmd_state)
    await message.answer(
        "Отлично!\nВыбери команду.",
        reply_markup=make_row_keyboard(available_currency_cmd),
    )


@currency_router.message(Command("custom"))
@currency_router.message(Currency.currency_cmd_state, F.text.casefold() == "custom")
async def process_custom(message: Message, state: FSMContext) -> None:
    await state.set_state(Currency.custom_state)
    log(message)
    await message.answer("Введи диапазон в днях.",
                         reply_markup=ReplyKeyboardRemove(),
                         )
    #data = await state.get_data()


@currency_router.message(Currency.custom_state)
async def process_chosing_custom(message: Message, state: FSMContext) -> None:
    log(message)
    my_range = message.text

    if my_range.isdigit() and 0 < int(my_range) <= 2000:
        await state.update_data(my_range=my_range)
        await state.set_state(Currency.currency_cmd_state)
        await message.answer(
            "Отлично!\nВыбери команду.",
            reply_markup=make_row_keyboard(available_currency_cmd),
        )
    else:
        await message.answer("Необходимо ввести целое число от 1 до 2000")
        await state.set_state(Currency.custom_state)
        await message.answer("Введи диапазон в днях.",
                             reply_markup=ReplyKeyboardRemove(),
                             )


async def show_result(message: Message, data: Dict[str, Any]) -> None:
    my_range = data.get("my_range", "no key <my_range>")
    currency = data.get("currency", "no key <currency>")
    currency_cmd = data.get("currency_cmd", "no key <currency_cmd>")
    await message.reply(text='Делаю запрос, пожалуйста, подождите.',
                        reply_markup=ReplyKeyboardRemove())

    if currency_cmd == "high":
        result = high(currency.lower()+'usdt', my_range)
        cmd_value = 'Максимальное'
    elif currency_cmd == "low":
        result = low(currency.lower() + 'usdt', my_range)
        cmd_value = 'Минимальное'
    else:
        await message.answer("Не выбрана команда /low или /high")
        result = None

    if result:
        text = f"{cmd_value} значение {currency} за {my_range} " \
               f"предыдущих дней - {result} usd."
    else:
        text = "Не удалось получить ответ от сервера."

    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())








