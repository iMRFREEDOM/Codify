from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, ConversationHandler
from database import Database
from register import check
from messages import message_handler
from inlines import inline_handler

TOKEN = ""

db = Database("db-evos.db")


def start_handler(update, context):
    check(update, context)


def contact_handler(update, context):
    message = update.message.contact.phone_number
    user = update.message.from_user
    # db_user = db.get_user_by_chat_id(user.id)
    db.update_user_data(user.id, "phone_number",message)
    check(update,context)

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_handler))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))
    dispatcher.add_handler(CallbackQueryHandler(inline_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
