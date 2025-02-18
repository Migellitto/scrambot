"""
файл с хэндлерами different_types.py, где просто будем выводить тип сообщения:
"""
from aiogram import Router, F
from aiogram.types import Message

true_users = [463644578,]
router = Router()

@router.message(F.text)
async def message_with_text(message: Message):
    await message.answer("Это просто долбанное текстовое сообщение!")

@router.message(F.sticker)
async def message_with_sticker(message: Message):
    await message.answer("Это просто долбанный стикер!")

@router.message(F.animation)
async def message_with_gif(message: Message):
    await message.answer("Это просто долбанный GIF!")