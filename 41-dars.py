# ConversationHandler
# ConversationHandler, geocopy orqali lokatsiyada address olish
# from geopy.geocoders import Nominatim
# def get_location_name(latitude, longitude):
#     geolocator = Nominatim(user_agent="my_app")
#     location = geolocator.reverse(f"{latitude}, {longitude}")
#     return location.address

# print(get_location_name(41, 70))

#####################################


import logging 
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import sqlite3
from geo_name import get_location_name

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS users
            (phone_number TEXT PRIMARY KEY, 
            first_name TEXT, 
            last_name TEXT, 
            age INTEGER, 
            gender TEXT, 
            address TEXT, 
            latitude REAL,
            longitude REAL
            );
""")
conn.commit()


def start(update, context):
    reply_text = 'Salom! telefon raqamingizni kiriting:'
    reply_markup = ReplyKeyboardMarkup([
        [KeyboardButton(text="Telefon kontaktinngizni ulashing", request_contact=True)]
    ], resize_keyboard=True, one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id, text=reply_text, reply_markup=reply_markup)
    logging.info(f"user - {update.effective_user.id} started")

    return 'PHONE_NUMBER'


def phone_number(update, context):
    phone_number = update.message.contact.phone_number
    context.user_data['phone_number'] = phone_number
    update.message.reply_text('Rahmat! Ismingiz nima?')
    return 'FIRST_NAME'


def first_name(update, context):
    first_name = update.message.text
    context.user_data['first_name'] = first_name
    update.message.reply_text('Rahmat! Familyangiz nima?')
    return 'LAST_NAME'


def last_name(update, context):
    last_name = update.message.text
    context.user_data['last_name'] = last_name
    update.message.reply_text('Rahmat! yoshingiz?')
    return 'AGE'


def age(update, context):
    age = update.message.text
    context.user_data['age'] = age
    update.message.reply_text('Rahmat! Jinsingiz: erkak/ayol?')
    return 'GENDER'


def gender(update, context):
    gender = update.message.text
    context.user_data['gender'] = gender
    reply_markup = ReplyKeyboardMarkup([
        [KeyboardButton(text="lokatsiyanngizni ulashing", request_location=True)]
    ], resize_keyboard=True, one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id, text="lokatsiyanngizni ulashing:", reply_markup=reply_markup)
    return 'GEOLOCATION'


def geolocation(update, context):
    latitude = update.message.location.latitude
    longitude = update.message.location.longitude
    address = get_location_name(latitude, longitude)
    context.user_data['latitude'] = latitude
    context.user_data['longitude'] = longitude
    context.user_data['address'] = address

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?,?)", (
        context.user_data['phone_number'],
        context.user_data['first_name'],
        context.user_data['last_name'],
        context.user_data['age'],
        context.user_data['gender'],
        context.user_data['address'],
        context.user_data['latitude'],
        context.user_data['longitude'],
    )
              )
    conn.commit()
    conn.close()
    logging.info("User Registered")
    update.message.reply_text("Ro'yxatdan o'tganingiz uchun Rahmat!")
    update.message.reply_text(f"""
        phone: {context.user_data['phone_number']},
        first_name: {context.user_data['first_name']},
        last_name: {context.user_data['last_name']},
        age: {context.user_data['age']},
        gender: {context.user_data['gender']},
        address: {context.user_data['address']},
        """)
    return ConversationHandler.END


def cancel(update, context):
    update.message.reply_text(text='Bekor qilindi!')
    return ConversationHandler.END


def main():
    updater = Updater(token="8672321253:AAGd64JBsncvelWyTIYjBTlIyqC6EaNdvz0")
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            'PHONE_NUMBER': [MessageHandler(Filters.contact & ~Filters.command, phone_number)],
            'FIRST_NAME': [MessageHandler(Filters.text & ~Filters.command, first_name)],
            'LAST_NAME': [MessageHandler(Filters.text & ~Filters.command, last_name)],
            'AGE': [MessageHandler(Filters.text & ~Filters.command, age)],
            'GENDER': [MessageHandler(Filters.text & ~Filters.command, gender)],
            'GEOLOCATION': [MessageHandler(Filters.location & ~Filters.command, geolocation)],

        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    dispatcher.add_handler(conv_handler)
    updater.start_polling()


if __name__ == '__main__':
    main()
