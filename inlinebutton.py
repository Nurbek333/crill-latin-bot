from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_translation_buttons():
    # Lotin matnlarini turli yozuvlarga tarjima qilish variantlari
    translation_buttons = [
        InlineKeyboardButton(text="🔤 Lotin -> Кирилл", callback_data='crill'),
        InlineKeyboardButton(text="🔤 Lotin -> Arab", callback_data='arab'),
        InlineKeyboardButton(text="🔤 Lotin -> Koreys", callback_data='kores')
    ]

    # Savollar va takliflar tugmasi
    savol_takliflar_button = InlineKeyboardButton(text="✉️ Savollar va takliflar", callback_data='savol_takliflar')

    # InlineKeyboardBuilder yordamida klaviatura yaratish
    keyboard = InlineKeyboardBuilder()

    # Tarjima tugmalarini bir qatorda joylashtirish
    keyboard.row(*translation_buttons)

    # Savollar va takliflar tugmasini yangi qatorda joylashtirish
    keyboard.row(savol_takliflar_button)

    # Klaviaturani markup sifatida qaytarish
    return keyboard.as_markup()
