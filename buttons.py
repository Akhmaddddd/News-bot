from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from configs import CATEGORIES


def butons_for_news():
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = []

    for category in CATEGORIES.keys():
        btn = KeyboardButton(text=category)
        buttons.append(btn)

    markup.add(*buttons)
    return markup


def btn_link(link):
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton(text='Читать полностью', url=link)
    )
    return markup










