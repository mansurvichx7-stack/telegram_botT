import asyncio
import logging
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram import Dispatcher, Bot, F
from aiogram.filters import CommandStart
from main import bot_token,menyu,saqlash,contact_kb,menyu2
from states import malumot_yigish
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
logging.basicConfig(level=logging.INFO)

bot = Bot(token=bot_token)



dp = Dispatcher(storage=MemoryStorage())
@dp.message(F.contact)
async def contact_handler(message: Message, state: FSMContext):
    contact_number = message.contact.phone_number
    await state.update_data(kontakt=contact_number)
    saqlash(
        telegram_id=message.from_user.id,
        foydalanuvchi_nomi=message.from_user.username,
        toliq_ism=None,
        kontakt=contact_number,
        qoshimcha_telefon=None,
        savolar=None,
        javoblar=None,
    )

    await message.answer("Rahmat, kontaktingiz qabul qilindi.", reply_markup=ReplyKeyboardRemove())
    await message.answer(
        "Assalomu alaykum! Botimizga xush kelibsiz. \nMenyudan o'zingizga kerakli bo'limni tanlang:",
        reply_markup=menyu
    )
    await message.delete()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Assalomu alaykum! Botimizga telefon raqamingizni yuborib boshlashingiz mumkin.",
        reply_markup=contact_kb
    )

@dp.callback_query(F.data == "sherik")
async def sherik_kerak(callback_query: CallbackQuery,state:FSMContext):
    await callback_query.answer()
    await callback_query.message.answer(
        "🤝 **Sherik topish uchun ariza**\n\n"
        "📋 Hozir sizga bir nechta savollar beriladi.\n"
        "✍️ Har bir savolga ketma-ket javob bering.\n\n"
        "✅ Barcha ma'lumotlar to‘g‘ri bo‘lsa,\n"
        "**HA** tugmasini bosish orqali arizangiz adminga yuboriladi."
    )
    await callback_query.message.answer("Ism, familiyangizni kiriting?")
    await state.set_state(malumot_yigish.familay_ism)
    await callback_query.message.delete()

@dp.message(malumot_yigish.familay_ism)
async def xabarbot(message:Message,state:FSMContext):
    await state.update_data(familay_ism=message.text)
    await message.answer(
    "📚 **Texnologiyalar**\n\n"
    "🔧 Talab qilinadigan texnologiyalarni kiriting.\n"
    "✍️ Texnologiya nomlarini **vergul ( , )** bilan ajrating.\n\n"
    "📌 Masalan:\n"
    "`Java, C++, C#`"
)
    await state.set_state(malumot_yigish.texnologiya)
    await message.delete()
@dp.message(malumot_yigish.texnologiya)
async def tel(message:Message,state:FSMContext):
    await state.update_data(texno = message.text)
    await message.answer("📞 Iltimos, qo'shimcha telefon raqamingizni kiriting:")
    await state.set_state(malumot_yigish.aloqa)
    await message.delete()


@dp.message(malumot_yigish.aloqa)
async def aloqa_handler(message: Message, state: FSMContext):
    await state.update_data(telefon = message.text)
    await message.answer(
        "🌐 Hudud:\n\nQaysi hududdansiz? Viloyat nomi masalan:\n'Toshkent shahar' "
    )
    await state.set_state(malumot_yigish.hudud)
    await message.delete()
@dp.message(malumot_yigish.hudud)
async def hudud(message: Message, state: FSMContext):
    await state.update_data(hudud = message.text)
    await message.answer(
        "💰 Narxi:\n\nTo'lov qilasizmi yoki bepulmi? Agar to'lov bo'lsa, summani kiriting (masalan: 100000 UZS)"
    )
    await state.set_state(malumot_yigish.narxi)
    await message.delete()
@dp.message(malumot_yigish.narxi)
async def narxibot(message:Message,state:FSMContext):
    await state.update_data(narxi = message.text)
    await message.answer(
        "👨🏻‍💻 Kasbi:\n\nIshlaysizmi yoki o'qiyapsizmi? Masalan: Talaba, Dasturchi"
    )
    await state.set_state(malumot_yigish.kasbi)
    await message.delete()
@dp.message(malumot_yigish.kasbi)
async def kasbbot(message:Message,state:FSMContext):
    await state.update_data(kasbi = message.text)
    await message.answer(
        "🕰 Murojaat qilish vaqti:\n\nQaysi vaqtda murojaat qilish mumkin? Masalan: 9:00 - 18:00"
    )
    await state.set_state(malumot_yigish.vaqt)
    await message.delete()
@dp.message(malumot_yigish.vaqt)
async def vaqtbot(message:Message,state:FSMContext):
    await state.update_data(vaqt = message.text)
    await message.answer(
        "🔎 Maqsad:\n\nMaqsadingizni qisqacha yozib bering. (Nima uchun sherik kerak, qanday ishlar bajariladi?)"
    )
    await state.set_state(malumot_yigish.maqsad)
    await message.delete()
@dp.message(malumot_yigish.maqsad)
async def maqsad(message:Message,state:FSMContext):
    await state.update_data(maqsad = message.text)
    await message.answer(
        "✅ Arizangiz tayyor\n\nAdminga yuborilsinmi?",
        reply_markup=menyu2
    )
    await state.set_state(malumot_yigish.tasdiq)
    await message.delete()
@dp.message(malumot_yigish.tasdiq, F.text.lower() == "ha")
async def tasdiqlash(message: Message, state: FSMContext):
    data = await state.get_data()
    saqlash(
        telegram_id=message.from_user.id,
        foydalanuvchi_nomi=message.from_user.username,
        toliq_ism=data.get("familay_ism"),
        kontakt=data.get("kontakt"),                     
        qoshimcha_telefon=data.get("telefon"),            
        savolar=[
            "Texnologiya",
            "Hudud",
            "Narxi",
            "Kasbi",
            "Vaqt",
            "Maqsad"
        ],
        javoblar={
            "texnologiya": data.get("texno"),
            "hudud": data.get("hudud"),
            "narxi": data.get("narxi"),
            "kasbi": data.get("kasbi"),
            "vaqt": data.get("vaqt"),
            "maqsad": data.get("maqsad")
        }
    )

    await message.answer("Arizangiz adminga yuborildi. Tez orada siz bilan bog'lanishadi.", reply_markup=ReplyKeyboardRemove())
    await state.clear()

@dp.message(malumot_yigish.tasdiq, F.text.lower() == "yoq")
async def yoq(message: Message, state: FSMContext):
    await message.answer("Arizangiz bekor qilindi.", reply_markup=ReplyKeyboardRemove())
    await state.clear()
async def main():
    await bot.send_message(chat_id=6611222144, text="Bot ishga tushdi")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())