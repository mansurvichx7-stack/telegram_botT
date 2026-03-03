from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
admin = '@rajabov_shohruhbek'

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

menyu = InlineKeyboardMarkup(
    inline_keyboard=[
        [  
            InlineKeyboardButton(text="Menyu 🍕", callback_data="menyu"),
            InlineKeyboardButton(text="Men haqimda", web_app=WebAppInfo(url="https://sadullaevmansurbek58-ctrl.github.io/murod-portfolio/"))
        ],
        [  
            InlineKeyboardButton(text="Bog'lanish", callback_data="boglanish")
        ]
    ]
)

def admin1():
    b1 = InlineKeyboardBuilder()
    b1.adjust(2)
    b1.add(InlineKeyboardButton(text="⬅️ Orqaga", callback_data="orqaga"))
    return b1.as_markup()


def menyubot(menyu):
    b = InlineKeyboardBuilder()
    for name in menyu:
        b.add(InlineKeyboardButton(text=f"{name['nomi']}", callback_data=f"{name['nomi']}"))
    b.adjust(2)
    b.add(InlineKeyboardButton(text="⬅️ Orqaga", callback_data="orqaga"))
    return b.as_markup()
    

def sonlarbot():
    b = InlineKeyboardBuilder()
    for i in range(1,10):
        b.add(InlineKeyboardButton(text=f"{i}", callback_data=f"{i}"))
    b.adjust(3)
    b.add(InlineKeyboardButton(text="⬅️ Orqaga", callback_data="orqaga"))
    return b.as_markup()
    