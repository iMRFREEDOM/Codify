from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from database import add_admin, add_student, save_student_photo, get_room_id_by_number
from config import SUPER_ADMIN_ID, CHOOSING_ROOM, CHOOSING_STUDENT, WAITING_PHOTO

async def add_admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != SUPER_ADMIN_ID:
        await update.message.reply_text("Siz super admin emassiz!")
        return
    args = context.args
    if not args:
        await update.message.reply_text("Ishlatish: /adminqoshish [Telegram_ID]")
        return
    try:
        new_id = int(args[0])
        if add_admin(new_id):
            await update.message.reply_text("Yangi admin qo'shildi!")
        else:
            await update.message.reply_text("Bu admin allaqachon mavjud.")
    except ValueError:
        await update.message.reply_text("ID raqam bo'lishi kerak.")

async def add_student_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != SUPER_ADMIN_ID:
        await update.message.reply_text("Sizda bunday huquq yo'q!")
        return
    args = context.args
    if len(args) < 3:
        await update.message.reply_text("Ishlatish: /oquvchiqoshish [Ism] [Familiya] [Xona_raqami]")
        return
    name, surname, room_num = args[0], args[1], args[2]
    room_id = get_room_id_by_number(room_num)
    if room_id:
        add_student(name, surname, room_id)
        await update.message.reply_text(f"O'quvchi {name} {surname} {room_num}-xonaga qo'shildi.")
    else:
        await update.message.reply_text("Bunday xona topilmadi.")