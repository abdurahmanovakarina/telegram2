import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import TOKEN
from app.handlers import router
from app.database.models import start_db
from app.parse import get_all

async def main():
    await start_db()
    bot = Bot(token = TOKEN, parse_mode='HTML')
    dp = Dispatcher()
    dp.include_router(router)
    #await get_all()
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
