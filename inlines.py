from telegram import InlineKeyboardButton, InlineKeyboardMarkup

import methods
from database import Database
import globals

db = Database("db-evos.db")

# Lesson-2 ###############
def inline_handler(update, context):

    query = update.callback_query
    data_sp = str(query.data).split("_")
    db_user = db.get_user_by_chat_id(query.message.chat_id)

    if data_sp[0] == "category":
# Lesson-3 ######################
        if data_sp[1] == "product":
            if data_sp[2] == "back":
                query.message.delete()
                products = db.get_products_by_category(category_id=int(data_sp[3]))
                buttons = methods.send_product_buttons(products=products, lang_id=db_user["lang_id"])

                clicked_btn = db.get_category_parent(int(data_sp[3]))

                if clicked_btn and clicked_btn['parent_id']:
                    buttons.append([InlineKeyboardButton(
                        text="Back", callback_data=f"category_back_{clicked_btn['parent_id']}"
                    )])
                else:
                    buttons.append([InlineKeyboardButton(
                        text="Back", callback_data=f"category_back"
                    )])

                query.message.reply_text(
                    text=globals.TEXT_ORDER[db_user['lang_id']],
                    reply_markup=InlineKeyboardMarkup(
                        inline_keyboard=buttons,
                    )
                )
            else:
                product = db.get_product_by_id(int(data_sp[2]))
                query.message.delete()

                caption = f"{globals.TEXT_PRODUCT_PRICE[db_user['lang_id']]} " + str(product["price"]) + \
                          f"\n{globals.TEXT_PRODUCT_DESC[db_user['lang_id']]}" + \
                          product[f"description_{globals.LANGUAGE_CODE[db_user['lang_id']]}"]

                buttons = [
                    [
                        InlineKeyboardButton(
                            text="1️⃣",
                            callback_data=f"category_product_{data_sp[2]}_{1}"
                        ),
                        InlineKeyboardButton(
                            text="2️⃣",
                            callback_data=f"category_product_{data_sp[2]}_{2}"
                        ),
                        InlineKeyboardButton(
                            text="3️⃣",
                            callback_data=f"category_product_{data_sp[2]}_{3}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="4️⃣",
                            callback_data=f"category_product_{data_sp[2]}_{4}"
                        ),
                        InlineKeyboardButton(
                            text="5️⃣",
                            callback_data=f"category_product_{data_sp[2]}_{5}"
                        ),
                        InlineKeyboardButton(
                            text="6️⃣",
                            callback_data=f"category_product_{data_sp[2]}_{6}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="7️⃣",
                            callback_data=f"category_product_{data_sp[2]}_{7}"
                        ),
                        InlineKeyboardButton(
                            text="8️⃣",
                            callback_data=f"category_product_{data_sp[2]}_{8}"
                        ),
                        InlineKeyboardButton(
                            text="9️⃣",
                            callback_data=f"category_product_{data_sp[2]}_{9}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="Back",
                            callback_data=f"category_product_back_{product['category_id']}"
                        )
                    ]
                ]

                query.message.reply_photo(
                    photo=open(product['image'], "rb"),
                    caption=caption,
                    reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons)
                )
################################
        elif data_sp[1] == "back":
            if len(data_sp) == 3:
                parent_id = int(data_sp[2])
            else:
                print("No parent")
                parent_id = None

            categories = db.get_categories_by_parent(parent_id=parent_id)
            buttons = []
            row = []
            for i in range(len(categories)):
                row.append(
                    InlineKeyboardButton(
                        text=categories[i][f'name_{globals.LANGUAGE_CODE[db_user["lang_id"]]}'],
                        callback_data=f"category_{categories[i]['id']}"
                    )
                )

                if len(row) == 2 or (len(categories) % 2 == 1 and i == len(categories) - 1):
                    buttons.append(row)
                    row = []

            if parent_id:
                clicked_btn = db.get_category_parent(parent_id)

                if clicked_btn and clicked_btn['parent_id']:
                    buttons.append([InlineKeyboardButton(
                        text="Back", callback_data=f"category_back_{clicked_btn['parent_id']}"
                    )])
                else:
                    buttons.append([InlineKeyboardButton(
                        text="Back", callback_data=f"category_back"
                    )])

            query.message.edit_reply_markup(
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=buttons
                )
            )
        else:
# lesson-3 #################################
            categories = db.get_categories_by_parent(parent_id=int(data_sp[1]))
            if categories:
                buttons = methods.send_category_buttons(categories=categories, lang_id=db_user["lang_id"])
            else:
                products = db.get_products_by_category(category_id=int(data_sp[1]))
                buttons = methods.send_product_buttons(products=products, lang_id=db_user["lang_id"])
############################################
            clicked_btn = db.get_category_parent(int(data_sp[1]))

            if clicked_btn and clicked_btn['parent_id']:
                buttons.append([InlineKeyboardButton(
                    text="Back", callback_data=f"category_back_{clicked_btn['parent_id']}"
                )])
            else:
                buttons.append([InlineKeyboardButton(
                    text="Back", callback_data=f"category_back"
                )])

            query.message.edit_reply_markup(
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=buttons
                )
            )
################################