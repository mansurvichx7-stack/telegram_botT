from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile, Message
from gtts import gTTS
from aiogram.fsm.context import FSMContext
from config_data.clasa_data import saqlsh
from tugmalar.inline_buttons.inline import  menu1
from tugmalar.reply_buttons.reply import contact

admin = '6611222144'  
contact1 = Router()

@contact1.callback_query(F.data == "boglanish")
async def boglanish(callback: CallbackQuery, state:FSMContext):
    await callback.message.answer( "✍️ Iltimos, ism-familiyangizni yozing:")
    await state.set_state(saqlsh.ism)


@contact1.message(saqlsh.ism)
async def ism(message: Message, state: FSMContext):
    await state.update_data(ism=message.text)
    await message.answer("📞 endi Telefon raqamingizni yuboring:", reply_markup=contact)
    if not message.contact:
        await message.answer("❌ Iltimos, telefon raqamingizni yuboring.")
    await state.set_state(saqlsh.tel)


@contact1.message(saqlsh.tel)
async def get_phone(message: Message, state: FSMContext):
    await state.update_data(telefon=message.contact.phone_number)

    await message.answer(
        "📝 Endi arizangizni yozib yuborishingiz mumkin:"
    )
    await state.set_state(saqlsh.ariza)



@contact1.message(saqlsh.ariza)
async def get_ariza(message: Message, state: FSMContext):
    data = await state.get_data()
    ism1 = data.get("ism")
    telefon1 = data.get("telefon")
    ariz1a = message.text
    await message.bot.send_message(chat_id=admin, text=f"Yangi ariza:\nIsm: {ism1}\nTelefon: {telefon1}\nAriza: {ariz1a}")
    await message.answer(
        "✅ Arizangiz qabul qilindi! Tez orada siz bilan bog'lanamiz.",
        reply_markup=menu1
    )
    await state.clear()

    














