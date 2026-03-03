from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

menu1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📚 Wiki qidiruv",
                callback_data="wiki"
            ),
            InlineKeyboardButton(
                text="🌍 Tarjima",
                callback_data="tarjimon"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ℹ️ Men haqimda",
                web_app=WebAppInfo(
                    url="https://sadullaevmansurbek58-ctrl.github.io/murod-portfolio/"
                )
            ),
        ],
        [
            InlineKeyboardButton(
                text="📞 Bog‘lanish",
                callback_data="boglanish"
            ),
        ],
    ]
)


orqaga = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🔙 Ortga",
                callback_data="orqaga"
            )]])