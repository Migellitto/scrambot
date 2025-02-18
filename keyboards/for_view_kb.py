"""
Начнём с клавиатуры: создадим рядом с файлом bot.py каталог keyboards,
 а внутри него файл for_questions.py и напишем функцию для получения
 простой клавиатуры с кнопками "Да" и "Нет" в один ряд:
"""

from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def view_action() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Текущий месяц")
    kb.button(text="Предыдущий месяц")
    kb.button(text="Все записи за полгода")
    kb.adjust(3)
    return kb.as_markup(resize_keyboard=True)