from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile, Message
from aiogram.fsm.context import FSMContext
from config_data.clasa_data import saqlsh
from tugmalar.inline_buttons.inline import orqaga, menu1
import wikipedia
wikipedia.set_lang('uz')

router = Router()



@router.callback_query(F.data == "wiki")
async def wikibot(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        "📚 Wikipedia qidiruv\n\nIltimos, so‘zni yozing 👇"
    )
    await state.set_state(saqlsh.qidruv)
    


@router.message(saqlsh.qidruv)
async def qidruv(message:Message,state: FSMContext):
    quti = message.text
    try:
        a = wikipedia.summary(quti)
        await message.answer(
                        f"📚 {quti} haqida ma’lumot:\n\n{a}",reply_markup=orqaga)
        await message.delete()
    except:
        await message.answer(
    "❌  Hech narsa topilmadi. \nIltimos, boshqa so‘z bilan urinib ko‘ring.",reply_markup=orqaga)
        
        
@router.callback_query(F.data == "orqaga")
async def orqagaBOT(callback: CallbackQuery,state: FSMContext):
    await callback.answer("🔙 Asosiy menyuga qaytdingiz", cache_time=True)
    await callback.message.answer("""🧭 Asosiy menyu\n\nQuyidagi tugmalardan birini tanlang 👇""", reply_markup=menu1)
    await callback.message.delete()

