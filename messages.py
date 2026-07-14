import methods
from register import check, check_data_decorator
from database import Database
import globals
from telegram import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

db = Database("db-evos.db")


@check_data_decorator
def message_handler(update, context):
    message = update.message.text
    user = update.message.from_user
    state = context.user_data.get("state", 0)
    db_user = db.get_user_by_chat_id(user.id)
    if state == 0:
        check(update, context)

    elif state == 1:
        if not db_user["lang_id"]:

            if message == globals.BTN_LANG_UZ:
                db.update_user_data(user.id, "lang_id", 1)
                check(update, context)

            elif message == globals.BTN_LANG_RU:
                db.update_user_data(user.id, "lang_id", 2)
                check(update, context)

            else:
                update.message.reply_text(
                    text=globals.TEXT_LANG_WARNING
                )

        elif not db_user["first_name"]:
            db.update_user_data(user.id, "first_name", message)
            check(update, context)

        elif not db_user["last_name"]:
            db.update_user_data(user.id, "last_name", message)
            buttons = [
                [KeyboardButton(text=globals.BTN_SEND_CONTACT[db_user['lang_id']], request_contact=True)]
            ]
            check(update, context)

        elif not db_user["phone_number"]:
            db.update_user_data(user.id, "phone_number", message)
            check(update, context)

        else:
            check(update, context)

################## lesson-2 ###################
    elif state == 2:
        if message == globals.BTN_ORDER[db_user['lang_id']]:
            categories = db.get_categories_by_parent()
# lesson-3 ###################
            buttons = methods.send_category_buttons(categories=categories, lang_id=db_user["lang_id"])
#############################################
            update.message.reply_text(
                text=globals.TEXT_ORDER[db_user['lang_id']],
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=buttons,
                )
            )
#############################################
    else:
        update.message.reply_text("Salom")
