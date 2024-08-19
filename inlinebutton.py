from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_translation_buttons():
    # Translation options
    translation_buttons = [
        InlineKeyboardButton(text="Кирилл", callback_data='crill'),
        InlineKeyboardButton(text="Араб", callback_data='arab'),
        InlineKeyboardButton(text="Корея", callback_data='kores')
    ]

    # Cancel button
    cancel_button = InlineKeyboardButton(text="Tilni almashtirish", callback_data='cancel')

    # Create an InlineKeyboardBuilder instance
    keyboard = InlineKeyboardBuilder()

    # Add translation buttons to the keyboard
    keyboard.add(*translation_buttons)
    
 

    # Return the keyboard as a markup
    return keyboard.as_markup()
