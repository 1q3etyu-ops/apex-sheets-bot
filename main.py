import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
TOKEN = "8965323255:AAGvz92nrEPe6TTewryY3bjBjmOEYqmxdRM"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    welcome_message = (
        f"أهلاً بك يا {user_name} في متجر Apex Sheets!\n\n"
        "احصل الآن على ملف الأوراق الاحترافي بسعر مميز جداً:\n"
        "السعر: 5.00 USDT\n"
        "شبكة الدفع: BNB Smart Chain (BEP20)\n\n"
        "عنوان المحفظة لتحويل المبلغ:\n"
        "0xYourWalletAddressHere\n\n"
        "ملاحظة هامة: بعد إتمام التحويل، أرسل صورة إيصال الدفع أو رقم المعاملة هنا، وسيتم إرسال الملف إليك مباشرة!"
    )
    await update.message.reply_text(welcome_message)
  def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
  
