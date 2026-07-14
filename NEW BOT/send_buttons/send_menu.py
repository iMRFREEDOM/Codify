from telegram import Update
from telegram.ext import ContextTypes
from database import is_admin_in_db, get_student_photo
from inlines import get_main_keyboard, get_rooms_inline, get_students_inline
from config import SUPER_ADMIN_ID

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    is_admin = is_admin_in_db(user_id)
    await update.message.reply_text(
        "Assalomu alaykum! Botga xush kelibsiz.",
        reply_markup=get_main_keyboard(user_id, is_admin)
    )

async def show_rooms(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Xonalarni tanlang:", reply_markup=get_rooms_inline())

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data.startswith("room_"):
        room_id = int(data.split("_")[1])
        await query.edit_message_text("O'quvchini tanlang:", reply_markup=get_students_inline(room_id))
    
    elif data == "back_rooms":
        await query.edit_message_text("Xonalarni tanlang:", reply_markup=get_rooms_inline())