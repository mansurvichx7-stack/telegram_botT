import asyncio
import logging
from config_data.config import bot_token
from aiogram import Bot, Dispatcher
from  handler.start import router1
from handler.wiki import router
from handler.translat import translate1
from handler.boglanish import contact1
from config_data.clasa_data import saqlsh


logging.basicConfig(level=logging.INFO)

bot = Bot(token=bot_token)
dp = Dispatcher()

dp.include_router(translate1)
dp.include_router(router) 
dp.include_router(router1) 
dp.include_router(contact1)

async def main():
    await bot.send_message(chat_id=6611222144,text="Bot ishga tushdi ✅")
    await dp.start_polling(bot)
 


if __name__ == "__main__":
    asyncio.run(main())



 