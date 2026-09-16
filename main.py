import os
import telebot
from telebot import types

TOKEN = "8965323255:AAGvz92nrEpE6TTewryY3_jB_eE9dJ3p8r4"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    welcome_text = f"مرحباً بك يا {user_name} في Apex Sheets!\n\nيمكنك الآن الحصول على ملف الأوراق الاحترافية بسعر مميز جداً:\n\nالسعر: USDT 5.00\nشبكة الدفع: BNB Smart Chain (BEP20)\nعنوان محفظة الأجرة:\n0xYourWalletAddressHere\n\nأرسل إيصال الدفع المقبول هنا، وسيتم إرسال الملف إليك مباشرة!"
    bot.reply_to(message, welcome_text)

def main():
    print("البوت قيد التشغيل...")
    bot.infinity_polling()

if __name__ == "__main__":
    main()
    
