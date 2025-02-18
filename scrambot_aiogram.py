import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from random import randrange
from handlers import start_router, view_router, different_types

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
token = '1693087967:AAEzgIK2_iK0zg6PnGTfk5ZfW6oof_fWXRw'
bot = Bot(token=token)
# Диспетчер
dp = Dispatcher()


dp.include_routers(start_router.router)
dp.include_routers(view_router.router)
dp.include_routers(different_types.router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
