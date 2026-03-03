t = '8067623156:AAGyLGb2UxtccUgOiNSyxfxkggdlDZshRho'
from datetime import datetime

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder 


cantact = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Kontakt jo'natish", request_contact=True)],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
menyu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Menyu 🍕"),
            KeyboardButton(text="men haqimda", web_app=WebAppInfo(url="https://sadullaevmansurbek58-ctrl.github.io/murod-portfolio/"))
        ]
    ],
    resize_keyboard=True
)


def mahsulot(menular):
    mahsulotlar = ReplyKeyboardBuilder()
    for menu in menular:    
        mahsulotlar.add(KeyboardButton(text=menu['nomi']))
    mahsulotlar.adjust(2)
    mahsulotlar.add(KeyboardButton(text="⬅️ Orqaga"))
    return mahsulotlar.as_markup(resize_keyboard=True)



def foydalanuvchi_bormi(telegram_id):
    a = connect('XenoAi.db')
    cursor = a.cursor()

    cursor.execute("""
        SELECT telefon_raqami FROM foydalanuvchilar
        WHERE telegram_id = ?
    """, (telegram_id,))

    natija = cursor.fetchone()
    a.close()

    if natija:
        return natija[0]  
    return None































from sqlite3 import connect
from datetime import datetime  


def saqlash(telegram_id, qidiruv_matni):
    a3 = connect('XenoAi.db')
    a12 = a3.cursor()

    a12.execute("""
    CREATE TABLE IF NOT EXISTS qidiruv_tarixi(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER NOT NULL,
        qidiruv_matni TEXT NOT NULL,
        sana DATETIME DEFAULT (DATETIME('now','localtime')),
        FOREIGN KEY (telegram_id) REFERENCES foydalanuvchilar(telegram_id)
    );
    """)

    hozir = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    a12.execute("""
        INSERT INTO qidiruv_tarixi(telegram_id, qidiruv_matni, sana)
        VALUES (?, ?, ?)
    """, (telegram_id, qidiruv_matni, hozir))

    a3.commit()
    a3.close()
    return 'yuklandi'


   





def adduser1(telegram_id,foydalanuvchi_nomi,toliq_ismi,telefon_raqami=None):
    a = connect('XenoAi.db')
    a1 = a.cursor()
    a1.execute("""
    CREATE TABLE IF NOT EXISTS foydalanuvchilar(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER UNIQUE NOT NULL,
        foydalanuvchi_nomi TEXT,
        toliq_ismi TEXT NOT NULL,
        telefon_raqami TEXT DEFAULT 'Noma''lum',
        rol TEXT DEFAULT 'foydalanuvchi',
        holati TEXT DEFAULT 'aktiv',
        royxatdan_otgan_sana DATETIME DEFAULT (DATETIME('now','localtime'))
);
    """)

    hozir1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    a1.execute("""
             INSERT OR IGNORE INTO foydalanuvchilar(telegram_id,foydalanuvchi_nomi,toliq_ismi,telefon_raqami,royxatdan_otgan_sana) values(?,?,?,?,?)
             """, (telegram_id,foydalanuvchi_nomi,toliq_ismi,telefon_raqami,hozir1))

    if telefon_raqami:
        a1.execute("""
            UPDATE foydalanuvchilar
            SET telefon_raqami = ?,
                foydalanuvchi_nomi = ?,
                toliq_ismi = ?
            WHERE telegram_id = ?
        """, (telefon_raqami, foydalanuvchi_nomi, toliq_ismi, telegram_id))

    a.commit()
    a.close()
    return 'yuklandi'




