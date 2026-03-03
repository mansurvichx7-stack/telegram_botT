import asyncio
from email import message
import logging
from aiogram import Bot, Dispatcher,F
from aiogram.types import Message,FSInputFile,CallbackQuery
from aiogram.filters import CommandStart
from telegram_ai import t, adduser1,saqlash,cantact,menyu,foydalanuvchi_bormi
import wikipedia
import json
from inline_buttons import menyu,menyubot,admin,sonlarbot,admin1
from telegram_ai import foydalanuvchi_bormi
wikipedia.set_lang('uz')

bot = Bot(token=t)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

@dp.message(CommandStart())
async def start_handler(message: Message):
    id1 = message.from_user.id
    tel = foydalanuvchi_bormi(id1)
    if tel :
         await message.answer( "Assalomu alaykum 👋 Xush kelibsiz!",reply_markup=menyu)
    else:
        await message.answer("Assalomu alaykum 👋 Iltimos kontaktni yuboring.", reply_markup=cantact)
        await message.delete()
         
@dp.message(F.contact)
async def contact_handler(message: Message):
     foydalanuvchi_id = message.from_user.id
     telefon = message.contact.phone_number if message.contact else None
     toliq_ismi = f"{message.from_user.first_name or ''} {message.from_user.last_name or ''}".strip()
     foydalanuvchi_nomi = message.from_user.first_name
     adduser1(
         foydalanuvchi_nomi=foydalanuvchi_nomi,
         telegram_id=foydalanuvchi_id,
         toliq_ismi=toliq_ismi,
         telefon_raqami=telefon
     )

     await message.answer("Rahmat, kontakt qabul qilindi.")
     await message.answer(
         "Assalomu alaykum, sizni botimizga xush kelibsiz. Siz menyuni tanlab mahsulotlarimizni ko'rishingiz mumkin",
         reply_markup=menyu
     )
     await message.delete()

@dp.callback_query()
async def MenyuBot1(call: CallbackQuery):
    text = call.data
    with open('mahsulot.json', 'r', encoding='utf-8') as f:
        mahsulotlar = json.load(f)

    if text == "menyu":
        await call.message.answer("Mahsulotlar ro'yxati", reply_markup=menyubot(mahsulotlar))
        await call.message.delete()
    if call.data == "boglanish":
        await call.message.answer(f"admin bilan boglanish: {admin}",reply_markup=admin1())
        await call.answer("admin shu inson ",show_alert=True)
        await call.message.delete()


    elif text == 'orqaga':
        await call.message.answer("Asosiy menyuga qaytdingiz", reply_markup=menyu)
        await call.answer("asosiy menyuga qaydingiz")
        await call.message.delete()

    else:
        for i in mahsulotlar:
            if i['nomi'].lower() == text.lower():
                await call.message.answer(f"{i['nomi']}\nnarxi: {i['narxi']}\nqancha olasiz:", reply_markup= sonlarbot())
                await call.message.delete()
                break
    if text.isdigit():
        await call.answer(text=f"{text} ta zakaz qilindi:", show_alert=True)
    else:
        text.isdigit()
        await call.answer(text=f"{text} xato malumot:", show_alert=True)
        
    saqlash(call.from_user.id, text)



async def main():
    await bot.send_message(chat_id=6611222144, text="Bot ishga tushdi")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())


