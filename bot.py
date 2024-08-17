import logging
import sys
import asyncio
import time
from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from data import config
from menucommands.set_bot_commands import set_default_commands
from baza.sqlite import Database
from filters.admin import IsBotAdminFilter
from filters.check_sub_channel import IsCheckSubChannels
from states.reklama import Adverts
from keyboard_buttons import admin_keyboard
from criltolatin import latindan_crill, latindan_arab, latindan_kores
from aiogram.fsm.state import State, StatesGroup

# Import the inline buttons from the separate file
from inlinebutton import get_translation_buttons

# Define the TranslationStates class here
class TranslationStates(StatesGroup):
    waiting_for_text = State()

ADMINS = config.ADMINS
TOKEN = config.BOT_TOKEN
CHANNELS = config.CHANNELS

dp = Dispatcher(storage=MemoryStorage())

@dp.message(CommandStart())
async def start_command(message: Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name, telegram_id=telegram_id)  # Add user to the database
        await message.answer(
            text="""Men [Bot nomi] botiman, sizga quyidagi funksiyalarni taqdim etaman:

2. **/about** - Bot haqidagi to'liq ma'lumot va yaratuvchilar haqida.
3. **/help** - Botning qanday ishlashini tushuntiruvchi yordam xabari.

**Qanday foydalanish kerak:**
- Ovozli xabarlarni yuborish uchun botga text jo'nating bot siz ovozli habarni tashlaydi.

Agar qo'shimcha savollar yoki yordam kerak bo'lsa, iltimos, [email:\nnurbekuktamov333@gmail.com/telegram username:\n@me_nurbek] orqali biz bilan bog'laning!

Botni ishlatganingiz uchun rahmat! 🎉
""", parse_mode=ParseMode.HTML, reply_markup=get_translation_buttons())
    except Exception as e:
        # logging.exception("Foydalanuvchini qo'shishda xatolik yuz berdi", e)
        await message.answer(text="""Men [Bot nomi] botiman, sizga quyidagi funksiyalarni taqdim etaman:

2. **/about** - Bot haqidagi to'liq ma'lumot va yaratuvchilar haqida.
3. **/help** - Botning qanday ishlashini tushuntiruvchi yordam xabari.

**Qanday foydalanish kerak:**
- Ovozli xabarlarni yuborish uchun botga text jo'nating bot siz ovozli habarni tashlaydi.

Agar qo'shimcha savollar yoki yordam kerak bo'lsa, iltimos, [email:\nnurbekuktamov333@gmail.com/telegram username:\n@me_nurbek] orqali biz bilan bog'laning!

Botni ishlatganingiz uchun rahmat! 🎉
""", parse_mode=ParseMode.HTML, reply_markup=get_translation_buttons())

@dp.callback_query(F.data.in_(['crill', 'arab', 'kores', 'cancel']))
async def handle_translation_callback(callback: CallbackQuery, state: FSMContext):
    if callback.data == 'cancel':
        await callback.message.answer("Transliteratsiya bekor qilindi. Endi yangi transliteratsiya tilini tanlashingiz mumkin.", reply_markup=get_translation_buttons())
        await state.clear()  # Clear the state if user cancels
    else:
        await callback.message.answer("Matnni yuboring:")
        await state.set_state(TranslationStates.waiting_for_text)
        await state.update_data(translation_type=callback.data)
        await callback.answer()  # Acknowledge the callback to prevent timeout

@dp.message(TranslationStates.waiting_for_text)
async def handle_text_input(message: Message, state: FSMContext):
    user_data = await state.get_data()
    translation_type = user_data.get('translation_type')
    input_text = message.text.lower()  # Convert text to lowercase

    if translation_type == 'crill':
        result_text = latindan_crill(input_text)
    elif translation_type == 'arab':
        result_text = latindan_arab(input_text)
    elif translation_type == 'kores':
        result_text = latindan_kores(input_text)
    else:
        result_text = "Noma'lum tarjima turi."

    await message.answer(result_text)
    # Send a follow-up message with the cancel button
    cancel_button = InlineKeyboardButton(text="❌ Bekor qilish", callback_data='cancel')
    keyboard = InlineKeyboardBuilder().add(cancel_button).as_markup()
    await message.answer("Yana matn yuborishingiz mumkin yoki ❌ Bekor qilish tugmasini bosing. Va yangi transliteratsiya tilini tanlang", reply_markup=keyboard)
    

@dp.message(IsCheckSubChannels())
async def kanalga_obuna(message: Message):
    text = ""
    inline_channel = InlineKeyboardBuilder()
    for index, channel in enumerate(CHANNELS):
        ChatInviteLink = await bot.create_chat_invite_link(channel)
        inline_channel.add(InlineKeyboardButton(text=f"{index+1}-kanal", url=ChatInviteLink.invite_link))
    inline_channel.adjust(1, repeat=True)
    button = inline_channel.as_markup()
    await message.answer(f"{text} kanallarga a'zo bo'ling", reply_markup=button)

@dp.message(Command("help"))
async def help_commands(message: Message):
    await message.answer("""👋 Salom! Transliteration Botdan qanday foydalanishni bilib oling:

1. **/crill** - Lotin matnini Kirill yozuviga o‘zgartiradi.  
   *Misol:* `/crill Salom` -> `Салом`
2. **/arab** - Lotin matnini Arab yozuviga o‘zgartiradi.  
   *Misol:* `/arab Salom` -> `سلام`
3. **/kores** - Lotin matnini Koreys yozuviga o‘zgartiradi.  
   *Misol:* `/kores Salom` -> `살롬`

Matnni ushbu komandalar bilan yuboring va kerakli yozuvga transliteratsiya qiling!

Agar qo'shimcha yordam yoki savollar bo'lsa, iltimos, [email:\nnurbekuktamov333@gmail.com/telegram:\n@me_nurbek] orqali biz bilan bog'laning!

""", parse_mode=ParseMode.HTML)

@dp.message(Command("about"))
async def about_commands(message: Message):
    await message.answer("""📢 **Bot Haqida:**

👋 **Salom! Men Transliteration Botman.**

**Yaratuvchi:** Nurbek Uktamov  
**Tajriba:** Backend dasturchi, Django bo'yicha mutaxassis  
**Maqsad:** Ushbu bot sizga Lotin matnini Kirill, Arab, va Koreys yozuvlariga transliteratsiya qilish uchun yaratilgan.

**Texnologiyalar:**  
- Python dasturlash tili  
- `aiogram` kutubxonasi  
- Maxsus transliteratsiya algoritmlari

**Kontakt:**  
Email: nurbekuktamov333@gmail.com  
Telegram: @me_nurbek

""", parse_mode=ParseMode.HTML)

@dp.message(Command("admin"), IsBotAdminFilter(ADMINS))
async def is_admin(message: Message):
    await message.answer(text="Admin menu", reply_markup=admin_keyboard.admin_button)

@dp.message(F.text == "Foydalanuvchilar soni", IsBotAdminFilter(ADMINS))
async def users_count(message: Message):
    counts = db.count_users()
    text = f"Botimizda {counts[0]} ta foydalanuvchi bor"
    await message.answer(text=text, parse_mode=ParseMode.HTML)

@dp.message(F.text == "Reklama yuborish", IsBotAdminFilter(ADMINS))
async def advert_dp(message: Message, state: FSMContext):
    await state.set_state(Adverts.adverts)
    await message.answer(text="Reklama yuborishingiz mumkin!", parse_mode=ParseMode.HTML)

@dp.message(Adverts.adverts)
async def send_advert(message: Message, state: FSMContext):
    message_id = message.message_id
    from_chat_id = message.from_user.id
    users = db.all_users_id()
    count = 0
    for user in users:
        try:
            await bot.copy_message(chat_id=user[0], from_chat_id=from_chat_id, message_id=message_id)
            count += 1
        except Exception as e:
            logging.exception(f"Foydalanuvchiga reklama yuborishda xatolik: {user[0]}", e)
        time.sleep(0.01)
    
    await message.answer(f"Reklama {count} ta foydalanuvchiga yuborildi", parse_mode=ParseMode.HTML)
    await state.clear()


# Define States
class TranslationStates(StatesGroup):
    waiting_for_text = State()

@dp.startup()
async def on_startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=int(admin), text="Bot ishga tushdi")
        except Exception as err:
            logging.exception(err)

@dp.shutdown()
async def off_startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=int(admin), text="Bot ishdan to'xtadi!")
        except Exception as err:
            logging.exception(err)

def setup_middlewares(dispatcher: Dispatcher, bot: Bot) -> None:
    from middlewares.throttling import ThrottlingMiddleware
    dispatcher.message.middleware(ThrottlingMiddleware(slow_mode_delay=0.5))

async def main() -> None:
    global bot, db
    bot = Bot(TOKEN)
    db = Database(path_to_db="main.db")
    await set_default_commands(bot)
    setup_middlewares(dispatcher=dp, bot=bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        stream=sys.stdout,
        format="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s"
    )
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.exception("Bot to'xtatildi!")
