from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from filters.group_chat import Isgroup
from loader import dp


@dp.message_handler(Isgroup(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name} guruhimizga xush kelibsiz!")


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}")

    