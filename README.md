# Transliteration Telegram Bot

Transliteration Telegram Bot'iga xush kelibsiz! Ushbu bot yordamida Latin matnini Kiril, Arab va Koreys yozuvlariga o'zgartirishingiz mumkin. Bu bot turli tillarda tez va oson transliteratsiya qilish uchun qulay vositadir.

## Xususiyatlar

- `/crill`: Latin matnini Kiril yozuviga o'zgartiradi.
- `/arab`: Latin matnini Arab yozuviga o'zgartiradi.
- `/kores`: Latin matnini Koreys yozuviga o'zgartiradi.


## Texnologiyalar

- Python 3.7 yoki undan yuqori versiya
- `aiogram` kutubxonasi
- Maxsus transliteratsiya algoritmlari


## O'rnatish

1. GitHub repozitoriyasini klonlang:

    ```bash
    git clone https://github.com/Nurbek333/crill-latin-bot.git
    cd your-repository
    ```

2. Virtual muhit yaratib, uni faollashtiring (ixtiyoriy):

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/MacOS
    venv\Scripts\activate     # Windows
    ```

3. Zaruriy kutubxonalarni o'rnating:

    ```bash
    pip install -r requirements.txt
    ```

4. `.env` faylini yaratib, Telegram bot tokenini qo'shing:

    ```
    BOT_TOKEN=your-telegram-bot-token
    ```



- **filters/**:
  - `admin.py`: Adminlar uchun maxsus funksiyalarni filtrlaydigan kodlar joylashgan.
  - `check_sub_channel.py`: Foydalanuvchining kerakli kanalga obuna bo‘lganligini tekshiruvchi kodlar.

- **keyboard_buttons/**:
  - `admin_keyboard.py`: Bot interfeysida adminlar uchun klaviatura tugmalari sozlanadi.

- **menucommands/**:
  - `set_bot_commands.py`: Telegram bot menyusidagi buyruqlarni o'rnatish uchun skript.
 

## Ishga tushirish

Botni ishga tushurish uchun:

```bash
python bot.py

