from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,MessageHandler,filters
from config import TOKEN
from database import create_tables
from keyboards import reply_markup

# /start komandasi kelganda bajariladigan oddiy funksiya
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Bot muvaffaqiyatli qayta yozilmoqda...",reply_markup=reply_markup)

def main():
    create_tables()
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("start"))

#############################
    print("Bot muvaffaqiyatli ishga tushdi...")
    # BOT TO'XTOVSIZ ISHLAYDI
    app.run_polling()

if __name__ == "__main__":
    main()