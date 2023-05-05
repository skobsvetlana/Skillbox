from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


inline_btn_low = InlineKeyboardButton('LOW', callback_data='LOW')
inline_kb_low = InlineKeyboardMarkup().add(inline_btn_low)


inline_btn_high = InlineKeyboardButton('HIGH', callback_data='HIGH')
inline_kb_high = InlineKeyboardMarkup().add(inline_btn_high)


# urlkb = InlineKeyboardMarkup(row_width=1)
# urlButton = InlineKeyboardButton(text='Перейти в блог Skillbox', url='https://skillbox.ru/media/code/')
# urlButton2 = InlineKeyboardButton(text='Перейти к курсам Skillbox', url='https://skillbox.ru/code/')
# urlkb.add(urlButton, urlButton2)


