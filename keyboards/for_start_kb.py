"""
Начнём с клавиатуры: создадим рядом с файлом bot.py каталог keyboards,
 а внутри него файл for_questions.py и напишем функцию для получения
 простой клавиатуры с кнопками "Да" и "Нет" в один ряд:
"""

from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from rest import get_month
from db.sqlite_db import sqlite_select_all, sqlite_select_all_task


def start_action() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Просмотр")
    kb.button(text="Добавление")
    kb.button(text="Удаление")
    kb.button(text="Пометить как выполненное")
    kb.button(text="Пометить как НЕвыполненное")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def tasks_list_done_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    data = sqlite_select_all(get_month()[0])
    for string in data:
        kb.button(text=f"✅ ID {string[0]}")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def tasks_list_fail_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    data = sqlite_select_all(get_month()[0])
    for string in data:
        kb.button(text=f"❌ ID {string[0]}")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def tasks_list_delete_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    data = sqlite_select_all(get_month()[0])
    for string in data:
        kb.button(text=f"🗑 ID {string[0]}")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)