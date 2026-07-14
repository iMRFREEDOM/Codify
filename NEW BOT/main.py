# main.py
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, 
    CallbackQueryHandler, ConversationHandler, filters
)
from database import create_tables
from config import TOKEN, ENTERING_DATE, WAITING_EXCEL_FILE
from send_buttons.send_menu import start_command, show_rooms, button_handler
from send_buttons.send_admin import add_admin_command, add_student_command
from send_buttons.send_grades import info_excel_command, date_received, excel_file_received

def main():
    create_tables()
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.Text(["Xonalarni ko'rish"]), show_rooms))
    app.add_handler(CommandHandler("adminqoshish", add_admin_command))
    app.add_handler(CommandHandler("oquvchiqoshish", add_student_command))
    app.add_handler(MessageHandler(filters.Text(["Admin qo'shish"]), add_admin_command))
    app.add_handler(MessageHandler(filters.Text(["O'quvchi qo'shish"]), add_student_command))

    grades_conv_handler = ConversationHandler(
        entry_points=[CommandHandler("info_excel", info_excel_command)],
        states={
            ENTERING_DATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, date_received)],
            WAITING_EXCEL_FILE: [MessageHandler(filters.Document.ALL, excel_file_received)],
        },
        fallbacks=[],
    )
    app.add_handler(grades_conv_handler)
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Bot muvaffaqiyatli ishga tushdi...")
    app.run_polling()
if __name__ == "__main__":
    main()