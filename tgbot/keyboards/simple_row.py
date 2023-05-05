from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def make_row_keyboard(items: list[str]) -> ReplyKeyboardMarkup:
    """
    Создаёт реплай-клавиатуру с кнопками в один ряд
    :param items: список текстов для кнопок
    :return: объект реплай-клавиатуры
    """
    row = [KeyboardButton(text=item) for item in items]
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True, one_time_keyboard=True)




# currency_btn = KeyboardButton(text="currency")
# history_btn = KeyboardButton(text="history")
# help_btn = KeyboardButton(text="help")
#
# start_keyboard = ReplyKeyboardMarkup(keyboard=[currency_btn,
#                                                history_btn,
#                                                help_btn],
#                                      resize_keyboard=True
#                                      )



# markup_currency_choice2 = ReplyKeyboardMarkup().row(
#     btn_currency_choice1, btn_currency_choice2)


# markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
#     KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
# ).add(
#     KeyboardButton('Отправить свою локацию 🗺️', request_location=True)
# )