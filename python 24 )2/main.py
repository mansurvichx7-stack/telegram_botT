bot_token = '8271090343:AAHhpnhtItbmrt3-8KrgUo6fLx6CYbBz5Zk'


from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from psycopg2 import Error, connect


from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menyu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🤝 Sherik kerak", callback_data="sherik"),
            InlineKeyboardButton(text="👨‍💼 Hodim kerak", callback_data="hodim")
        ],
        [
            InlineKeyboardButton(text="🏢 Ish joyi kerak", callback_data="ish joyi"),
            InlineKeyboardButton(text="🎓 Ustoz kerak", callback_data="ustoz")
        ],
        [
            InlineKeyboardButton(text="🧑‍🎓 Shogirt kerak", callback_data="shogirt")
        ]
    ]
)
menyu2 = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="ha"), KeyboardButton(text="yoq")]
    ], resize_keyboard=True, one_time_keyboard=True
)

contact_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📞 Kontaktni yuborish", request_contact=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
import json

def saqlash(telegram_id, foydalanuvchi_nomi, toliq_ism, kontakt, qoshimcha_telefon, savolar, javoblar):
    if savolar is not None:
        savolar = json.dumps(savolar, ensure_ascii=False)
    if javoblar is not None:
        javoblar = json.dumps(javoblar, ensure_ascii=False)
        
    try:
        d = connect(
            host="localhost",
            user="postgres",
            password="12345",
            database="python24",
            port="5432"
        )
        b = d.cursor()
        b.execute("""
            CREATE TABLE IF NOT EXISTS malumotlar_bazasi (
                id SERIAL PRIMARY KEY,
                telegram_id bigint unique,
                foydalanuvchi_nomi VARCHAR(255),
                toliq_ism VARCHAR(255),
                kontakt VARCHAR(255),
                qoshimcha_telefon VARCHAR(255),
                savolar VARCHAR(255),
                javoblar TEXT,
                yaratilgan_vaqt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        b.execute(""" INSERT INTO malumotlar_bazasi (
                telegram_id, foydalanuvchi_nomi, toliq_ism,
                kontakt, qoshimcha_telefon, savolar, javoblar
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (telegram_id) DO UPDATE
            SET foydalanuvchi_nomi = EXCLUDED.foydalanuvchi_nomi,
                toliq_ism = EXCLUDED.toliq_ism,
                kontakt = EXCLUDED.kontakt,
                qoshimcha_telefon = EXCLUDED.qoshimcha_telefon,
                savolar = EXCLUDED.savolar,
                javoblar = EXCLUDED.javoblar;
        """, (
            telegram_id,
            foydalanuvchi_nomi,
            toliq_ism,
            kontakt,
            qoshimcha_telefon,
            savolar,
            javoblar
        ))
        d.commit()
        b.close()
        d.close()
    except Error as e:
        print("xato: ",e)        
    
