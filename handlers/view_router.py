from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.enums import ParseMode
from keyboards.for_view_kb import view_action
from keyboards.for_start_kb import start_action
from check_user import check_users
import sqlalchemy as db
from db.sqlite_db import sqlite_select_all, sqlite_select_all_task
from rest import get_month

router = Router()

@router.message(Command("view"))
async def cmd_view(message: Message):
    if check_users(message.from_user.id) == True:
        await message.answer("За какой период смотрим?", reply_markup=view_action())
    else:
        await message.answer_dice(emoji="🎲")

@router.message(F.text.lower() == "текущий месяц")
async def answer_see(message: Message):
    if check_users(message.from_user.id) == True:
        await message.answer("Просмотр за текущий месяц:", reply_markup=ReplyKeyboardRemove())
        data = sqlite_select_all(get_month()[0])
        mess = ''
        for string in data:
            if string[3] == True:
                active = '❌'
            else:
                active = '✅'
            mess = f"{mess}\n\nДействие: {string[1]} - {active}; ID:{string[0]} (месяц {string[2]})"
        # print(mess)
        await message.answer(mess, reply_markup=start_action())

@router.message(F.text.lower() == "предыдущий месяц")
async def answer_see(message: Message):
    if check_users(message.from_user.id) == True:
        await message.answer("Просмотр за предыдущий месяц:", reply_markup=ReplyKeyboardRemove())
        data = sqlite_select_all(get_month()[1])
        mess = ''
        for string in data:
            if string[3] == True:
                active = '❌'
            else:
                active = '✅'
            mess = f"{mess}\n\nДействие: {string[1]} - {active}; ID:{string[0]} (месяц {string[2]})"
        # print(mess)
        await message.answer(mess, reply_markup=start_action())
@router.message(F.text.lower() == "все записи за полгода")
async def answer_see(message: Message):
    if check_users(message.from_user.id) == True:
        await message.answer("Просмотр за полгода:", reply_markup=ReplyKeyboardRemove())
        data = sqlite_select_all_task()
        mess = ''
        for string in data:
            if string[3] == True:
                active = '❌'
            else:
                active = '✅'
            mess = f"{mess}\n\nДействие: {string[1]} - {active}; ID:{string[0]} (месяц {string[2]})"
        # print(mess)
        await message.answer(mess, reply_markup=start_action())