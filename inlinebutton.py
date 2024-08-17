# inlinebutton.py
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_translation_buttons():
    # Create InlineKeyboardMarkup instance
    inline_kb = InlineKeyboardMarkup(row_width=1)
    # Define buttons
    buttons = [
        InlineKeyboardButton(text="Lotin ➔ Kirill", callback_data="crill"),
        InlineKeyboardButton(text="Lotin ➔ Arab", callback_data="arab"),
        InlineKeyboardButton(text="Lotin ➔ Koreys", callback_data="kores"),
    ]
    # Add buttons to the markup
    inline_kb.add(*buttons)
    return inline_kb
