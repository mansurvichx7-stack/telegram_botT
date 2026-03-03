from aiogram import Router,F
from aiogram.filters import CommandStart
from aiogram.types import Message,CallbackQuery
from aiogram.fsm.context import FSMContext
from tugmalar.inline_buttons.inline import menu1,orqaga
from config_data.clasa_data import saqlsh

router1 = Router()

@router1.message(CommandStart())
async def start_cmd(message: Message, state: FSMContext):
    await state.set_state(saqlsh.waiting_for_name)
    await message.answer("Assalomu alekum iltomis Ismingni kiriting 👇")

@router1.message(saqlsh.waiting_for_name)
async def get_name(message: Message, state: FSMContext):
    name = message.text
    await state.clear()

    await message.answer(
        f"😊 Tanishganimdan xursandman, {name}!",
        reply_markup=menu1
    )


    






