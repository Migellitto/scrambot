"""
рядом с файлом bot.py создадим другой каталог handlers, а внутри него файл questions.py.
Обратим внимание на пункты [1] и [2]. Во-первых, мы в файле создали свой собственный
роутер уровня модуля, и далее будем цеплять его к корневому роутеру (диспетчеру).
Во-вторых, хэндлеры «отпочковываются» уже от локального роутера.
"""
import re
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from keyboards.for_start_kb import start_action, tasks_list_done_kb, tasks_list_fail_kb
from keyboards.for_view_kb import view_action
from check_user import check_users
from db.sqlite_db import sqlite_task_id_update_0, sqlite_task_id_update_1, sqlite_insert_new_task

router = Router()  # [1]


class TaskName(StatesGroup):
    task_name = State()

@router.message(Command("start"))  # [2]
async def cmd_start(message: Message):
    if check_users(message.from_user.id) == True:
        await message.answer("Что надо?", reply_markup=start_action())
    else:
        await message.answer_dice(emoji="🎲")

@router.message(F.text.lower() == "просмотр")
async def answer_see(message: Message):
    if check_users(message.from_user.id) == True:
        await message.answer("Переход к /view", reply_markup=view_action())

@router.message(F.text.lower() == "добавление")
async def answer_add(message: Message, state: FSMContext):
    if check_users(message.from_user.id) == True:
        await message.answer("добавление таски",reply_markup=ReplyKeyboardRemove())
        await state.set_state(TaskName.task_name)
        await message.answer("Надо добавить имя таски")

@router.message(TaskName.task_name)
async def fsm_second_step(message: Message, state: FSMContext):
    await state.update_data(task_name=message.text)
    data = await state.get_data()
    sqlite_insert_new_task(str(data["task_name"]))
    await message.answer(f'Название таски: {data["task_name"]}; Статус: добавлено.', reply_markup=start_action())
    await state.clear()

@router.message(F.text.lower() == "удаление")
async def answer_del(message: Message):
    if check_users(message.from_user.id) == True:
        await message.answer("НЕ РАБОТАЕТ", reply_markup=ReplyKeyboardRemove())

@router.message(F.text.lower() == "пометить как выполненное")
async def answer_del(message: Message):
    if check_users(message.from_user.id) == True:
        await message.answer("Пометить как выполненное по ID ✅", reply_markup=tasks_list_done_kb())

@router.message(F.text.lower() == "пометить как невыполненное")
async def answer_del(message: Message):
    if check_users(message.from_user.id) == True:
        await message.answer("Пометить как НЕвыполненное по ID ❌", reply_markup=tasks_list_fail_kb())

@router.message(F.text.startswith("✅ ID "))
async def answer_del(message: Message):
    if check_users(message.from_user.id) == True:
        await message.answer(f"{message.text}", reply_markup=ReplyKeyboardRemove())
        task_id = int(re.sub("✅ ID ","",message.text))
        sqlite_task_id_update_0(task_id)
        await message.answer(f"task_id {task_id}", reply_markup=start_action())

@router.message(F.text.startswith("❌ ID "))
async def answer_del(message: Message):
    if check_users(message.from_user.id) == True:
        await message.answer(f"{message.text}", reply_markup=ReplyKeyboardRemove())
        task_id = int(re.sub("❌ ID ","",message.text))
        sqlite_task_id_update_1(task_id)
        await message.answer(f"task_id {task_id}", reply_markup=start_action())