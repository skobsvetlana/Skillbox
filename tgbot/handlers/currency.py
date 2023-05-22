import logging

from aiogram import Router, F
from aiogram.filters import Command, StateFilter, Text
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.utils.markdown import text, bold

from tgbot.keyboards.simple_row import make_row_keyboard
from tgbot.logger import log
from tgbot.messages import MESSAGES
from tgbot.history import get_history

from data_collection.high import get_max_high_value
from data_collection.low import get_mim_low_value

from typing import Any, Dict

currency_router = Router()

available_start_cmd = ["CURRENCY", "HISTORY", "HELP"]
available_currency = ["BTC", "ETH", "CANCEL"]
available_range_cmd = ["LAST DAY", "CUSTOM", "CANCEL"]
available_currency_cmd = ["LOW", "HIGH", "CANCEL"]

class Currency(StatesGroup):
    """
    Класс, наследуемый от StatesGroup, для группы состояний FSM.
    Создаем экземпляры класса State, последовательно
    перечисляя возможные состояния, в которых будет находиться
    бот в разные моменты взаимодейтсвия с пользователем
    common_cmd_state - состояние ожидания выбора стартовых команд,
    currency_state - состояние ожидания выбора криптовалюты,
    choosing_period_state - состояние ожидания выбора периода,
    custom_state - состояние ожидания ввода и контроля введенного значения
    периода
    last_day_state - состояние "период по умолчанию"
    currency_cmd_state - состояние ожидания выбора команды "минимального"
    или "максимального" значения.
    """

    start_cmd_state: State = State()
    currency_state: State = State()
    choosing_period_state = State()
    custom_state = State()
    last_day_state = State()
    currency_cmd_state = State()


@currency_router.message(Command("cancel"))
@currency_router.message(F.text.casefold() == "cancel")
async def cancel_handler(message: Message, state: FSMContext) -> None:
    """
    Этот хэндлер будет срабатывать на команду /cancel не зависимо от состояний,
    переводить в состояние ожидания выбора стартовых команд и предлагать выбать
    одну из стартовых команд, нажав на кнопку или отправив команду.
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
    await state.set_state(Currency.start_cmd_state)
    await message.answer(f"Выбери команду.",
                         reply_markup=make_row_keyboard(available_start_cmd))
    

@currency_router.message(Command("start"))
async def process_start_command(message: Message, state: FSMContext) -> None:
    """
    Этот хэндлер будет срабатывать на команду /start вне состояний,
    выводить приветственное сообщение, переводить в состояние ожидания
    выбора стартовых команд и предлагать выбать одну из стартовых команд,
    нажав на кнопку или отправив команду.
    """

    await message.answer(MESSAGES['start'],
                         reply_markup=make_row_keyboard(available_start_cmd))
    await state.set_state(Currency.start_cmd_state)


@currency_router.message(Command("currency"))
@currency_router.message(Currency.start_cmd_state, F.text.casefold() == "currency")
async def process_currency(message: Message, state: FSMContext) -> None:
    """
    Этот хэндлер будет срабатывать на команду /currency, переводить
    в состояние ожидания выбора криптовалюты и предлагать
    выбрать криптовалюту, нажав на кнопку или отправив
    команду.
    """

    log(message)
    await state.set_state(Currency.currency_state)
    await state.update_data(common_cmd=message.text)
    await message.answer(
        "Отлично!\nВыбери криптовалюту.",
        reply_markup=make_row_keyboard(available_currency),
    )

@currency_router.message(Command("history"))
@currency_router.message(Currency.start_cmd_state, F.text.casefold() == "history")
async def process_history(message: Message, state: FSMContext):
    """
    Этот хэндлер будет срабатывать на команду /history, запускать функцию,
    показывающую историю выполненных команд, переводить в состояние ожидания
    выбора стартовых команд и предлагать выбрать криптовалюту, нажав на кнопку или
    отправив команду.
    """

    log(message)
    user_id = message.from_user.id
    user_history = get_history(str(user_id))
    for el in user_history:
        await message.answer(text=str(el))
    await state.clear()
    await state.set_state(Currency.start_cmd_state)
    await message.answer(f"Выбери команду.",
                         reply_markup=make_row_keyboard(available_start_cmd))


@currency_router.message(Command("help"))
@currency_router.message(Currency.start_cmd_state, F.text.casefold() == "help")
async def process_help_command(message: Message, state: FSMContext):
    """
    Этот хэндлер будет срабатывать на команду /help, показывать описание возможных
    команд, переводить в состояние ожидания выбора стартовых команд и предлагать
    выбрать криптовалюту, нажав на кнопку или отправив команду.
    """

    log(message)
    await state.clear()
    msg = text(bold('Я могу ответить на следующие команды:'), '\n',
               MESSAGES['low'], MESSAGES['high'],
               MESSAGES['last_day'], MESSAGES['custom'],
               MESSAGES['currency'], MESSAGES['history'], sep='\n')
    await message.answer(msg, reply_markup=ReplyKeyboardRemove(),)
    await state.set_state(Currency.start_cmd_state)
    await message.answer(f"Выбери команду.",
                         reply_markup=make_row_keyboard(available_start_cmd))


@currency_router.message(Currency.start_cmd_state)
async def process_start_cmd_unknown_message(message: Message, state: FSMContext) -> None:
    """
    Этот хэндлер будет срабатывать в случае ввода команды не входящей в
    список стартовых команд, переводить в состояние ожидания
    выбора этих команд и предлагать выбать одну из команд,
    нажав на кнопку или отправив команду.
    """

    log(message)
    await state.set_state(Currency.start_cmd_state)
    await message.answer(text=MESSAGES["unknown_message"],
                         reply_markup=make_row_keyboard(available_start_cmd))


@currency_router.message(StateFilter(Currency.currency_state),
                         Text(text=available_currency))
async def process_choosing_currency(message: Message, state: FSMContext):
    """
    Этот хэндлер будет срабатывать на нажатие кнопки при выборе криптовалюты,
    переводить в состояние ожидания выбора периода и предлагать выбрать
    период, за который необходимо получить информацию, нажав на кнопку.
    """

    log(message)
    await state.set_state(Currency.choosing_period_state)
    await state.update_data(currency=message.text)
    await message.answer("Отлично!\nВыбери период")
    await message.answer(
        "Нажми LAST DAY, если хочешь получить информацию за последний прошедший день.\n\n"
        "Нажми CUSTOM, если хочешь выбрать интервал. Максимальный интервал - 2000 дней.",
        reply_markup=make_row_keyboard(available_range_cmd),
    )


@currency_router.message(StateFilter(Currency.currency_state))
async def process_choosing_currency(message: Message):
    """
    Этот хэндлер будет срабатывать, если во время выбора криптовалюты
    будет введено некорректное значение.
    """

    await message.answer(text=MESSAGES["unknown_message"])


@currency_router.message(Command("last_day"))
@currency_router.message(Currency.choosing_period_state,
                         F.text.casefold() == "last day")
async def process_custom(message: Message, state: FSMContext) -> None:
    """
    Этот хэндлер будет срабатывать на команду /last_day, переводить в
    состояние "период по умолчанию", переводить в состояние ожидания
    выбора команды "минимального" или "максимального" значения и
    предлагать выбрать, нажав на кнопку или отправив команду.
    """

    await state.set_state(Currency.last_day_state)
    log(message)
    await state.update_data(my_range=1)
    await state.set_state(Currency.currency_cmd_state)
    await message.answer(
        "Отлично!\nВыбери команду.",
        reply_markup=make_row_keyboard(available_currency_cmd),
    )


@currency_router.message(Command("custom"))
@currency_router.message(Currency.choosing_period_state, F.text.casefold() == "custom")
async def process_choosing_custom(message: Message, state: FSMContext) -> None:
    """
    Этот хэндлер будет срабатывать на команду /custom и переводить в
    состояние ожидания ввода периода.
    """

    await state.set_state(Currency.custom_state)
    log(message)
    await message.answer("Введи диапазон в днях.")


@currency_router.message(Currency.choosing_period_state)
async def process_choosing_period_unknown_message(message: Message, state: FSMContext) -> None:
    """
    Этот хэндлер будет срабатывать в случае ввода команды не входящей в
    список команд для выбора периода, переводить в состояние ожидания
    выбора этих команд и предлагать выбать одну из команд,
    нажав на кнопку или отправив команду.
    """

    log(message)
    await state.set_state(Currency.choosing_period_state)
    await message.answer(text=MESSAGES["unknown_message"],
                         reply_markup=make_row_keyboard(available_range_cmd))


@currency_router.message(StateFilter(Currency.custom_state),
                         lambda x: x.text.isdigit() and 0 < int(x.text) <= 2000)
async def checking_custom_period(message: Message, state: FSMContext) -> None:
    """
    Этот хэндлер будет срабатывать, если введено корректное значение
    периода и переводить в состояние ожидания выбора команды "минимального"
    или "максимального" значения.
    """

    log(message)
    await state.update_data(my_range=message.text)
    await state.set_state(Currency.currency_cmd_state)
    await message.answer(
        "Отлично!\nВыбери команду.",
        reply_markup=make_row_keyboard(available_currency_cmd),
    )


@currency_router.message(StateFilter(Currency.custom_state))
async def wrong_custom_period(message: Message):
    """
    Этот хэндлер будет срабатывать, если во время ввода периода
    будет введено некорректное знаение.
    """

    log(message)
    await message.answer(
        text='Период должен быть целым числом от 1 до 2000\n\n'
             'Попробуйте еще раз\n\nЕсли вы хотите вернуться'
             'в стартовое меню  - отправьте команду /cancel')


@currency_router.message(Command("low"))
@currency_router.message(Currency.currency_cmd_state, F.text.casefold() == "low")
async def process_low_cmd(message: Message, state: FSMContext) -> None:
    """
    Этот хэндлер будет срабатывать на команду /low, обрабатывать, полученные
    данные, выводить результат обработки, завершать машину состояний,
    переводить в состояние ожидания выбора стартовых команд и предлагать выбать
    одну из стартовых команд, нажав на кнопку или отправив команду.
    """

    log(message)
    data = await state.update_data(currency_cmd=message.text.lower())
    await show_result(message=message, data=data)
    await state.clear()
    await state.set_state(Currency.start_cmd_state)
    await message.answer(f"Выбери команду.",
                         reply_markup=make_row_keyboard(available_start_cmd))


@currency_router.message(Command("high"))
@currency_router.message(Currency.currency_cmd_state, F.text.casefold() == "high")
async def process_high_cmd(message: Message, state: FSMContext) -> None:
    """
    Этот хэндлер будет срабатывать на команду /high, обрабатывать, полученные
    данные, выводить результат обработки, завершать машину состояний,
    переводить в состояние ожидания выбора стартовых команд и предлагать выбать
    одну из стартовых команд, нажав на кнопку или отправив команду.
    """

    log(message)
    data = await state.update_data(currency_cmd=message.text.lower())
    await show_result(message=message, data=data)
    await state.clear()
    await state.set_state(Currency.start_cmd_state)
    await message.answer(f"Выбери команду.",
                         reply_markup=make_row_keyboard(available_start_cmd))


async def show_result(message: Message, data: Dict[str, Any]) -> None:
    """
    Функция вызывает функцию data_collection.high.get_max_high_value или
    data_collection.high.get_max_low_value с выбранными параметрами my_range и currency
    в зависимости от значения переменной currency_cmd - 'high' или 'low' соответственно.
    """

    my_range: int = data.get("my_range", "no key <my_range>")
    currency: str = data.get("currency", "no key <currency>")
    currency_cmd: str = data.get("currency_cmd", "no key <currency_cmd>")
    await message.reply(text='Делаю запрос, пожалуйста, подождите.',
                        reply_markup=ReplyKeyboardRemove())

    if currency_cmd == "high":
        result = get_max_high_value(currency.lower() + 'usdt', my_range)
        cmd_value = 'Максимальное'
    elif currency_cmd == "low":
        result = get_mim_low_value(currency.lower() + 'usdt', my_range)
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


@currency_router.message(Currency.currency_cmd_state)
async def process_currency_cmd_unknown_message(message: Message, state: FSMContext):
    """
    Этот хэндлер будет срабатывать в случае ввода команды не входящей в
    список команд для выбора минимального и максимального значений, переводить в
    состояние ожидания выбора этих команд и предлагать выбать одну из команд,
    нажав на кнопку или отправив команду.
    """

    log(message)
    await state.set_state(Currency.choosing_period_state)
    await message.answer(text=MESSAGES["unknown_message"],
                         reply_markup=make_row_keyboard(available_currency_cmd))






