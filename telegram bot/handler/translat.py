from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile, Message
from gtts import gTTS
from translate import Translator
from aiogram.fsm.context import FSMContext
from config_data.clasa_data import saqlsh
from tugmalar.inline_buttons.inline import orqaga, menu1

translate1 = Router()

@translate1.callback_query(F.data == "tarjimon")
async def TranslateBot(callback: CallbackQuery, state:FSMContext):
    await callback.message.answer(
        "🌍 Tarjimon ishga tushdi!\n\n"
        "✍️ O‘zbekcha matn yozing,\n"
        "men uni rus tiliga tarjima qilib beraman 👇"
    )
    await state.set_state(saqlsh.tarjima)
@translate1.message(saqlsh.tarjima)
async def tarjimabot(message: Message, state: FSMContext):
    xabar = message.text
    translator = Translator(from_lang='uz', to_lang="ru")
    tarjima = translator.translate(f"{xabar}")
    voice = gTTS(text=tarjima, lang='ru')
    voice.save('voice.mp3')
    musika = FSInputFile('voice.mp3')
    await message.answer_voice(voice=musika,caption=f"🇺🇿 → 🇷🇺 Tarjima:\n\n{tarjima}",
        reply_markup=orqaga
    )

