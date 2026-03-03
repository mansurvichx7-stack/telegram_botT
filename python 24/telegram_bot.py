import logging
import asyncio
from aiogram.types import Message
from aiogram import Dispatcher, Bot, F 
from aiogram.filters import CommandStart
from token2 import bot_token


logging.basicConfig(level=logging.INFO)
bot = Bot(token=bot_token)
dp = Dispatcher()
