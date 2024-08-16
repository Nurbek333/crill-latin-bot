Transliteration Telegram Bot
Transliteration Telegram Bot'iga xush kelibsiz! Ushbu bot yordamida Latin matnini Kiril, Arab va Koreys yozuvlariga o'zgartirishingiz mumkin. Bu bot turli tillarda tez va oson transliteratsiya qilish uchun qulay vositadir.

Xususiyatlar
/crill: Latin matnini Kiril yozuviga o'zgartiradi.
/arab: Latin matnini Arab yozuviga o'zgartiradi.
/kores: Latin matnini Koreys yozuviga o'zgartiradi.
Boshlash
Botni ishlatishni boshlash uchun quyidagi qadamlarni bajaring:

Repository'ni Klonlash

bash
Копировать код
git clone https://github.com/your-username/transliteration-bot.git
cd transliteration-bot
Zaruriy Paketlarni O'rnatish

Python 3.8+ versiyasi o'rnatilgan bo'lishi kerak. Zaruriy Python paketlarini pip yordamida o'rnating:

bash
Копировать код
pip install -r requirements.txt
Botni Sozlash

config.py faylini yarating va Telegram bot tokeningizni qo'shing:

python
Копировать код
TOKEN = 'YOUR_BOT_TOKEN'
Botni Ishga Tushurish

Botni ishga tushurish uchun:

bash
Копировать код
python bot.py
Buyruqlar
/crill: Ushbu buyruqni matningiz bilan birga ishlating va Latin yozuvini Kiril yozuviga o'zgartiring.
/arab: Ushbu buyruqni matningiz bilan birga ishlating va Latin yozuvini Arab yozuviga o'zgartiring.
/kores: Ushbu buyruqni matningiz bilan birga ishlating va Latin yozuvini Koreys yozuviga o'zgartiring.
Hissa Qo'shish
Takliflar yoki yaxshilanishlar bo'lsa, muammolarni oching yoki pull request yuboring.
