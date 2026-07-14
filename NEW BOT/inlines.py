from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from database import get_all_rooms, get_students_by_room
from config import SUPER_ADMIN_ID

def get_main_keyboard(user_id, is_admin):
    buttons = [["Xonalarni ko'rish"], ["Anonim fikrlar"]]
    if is_admin or user_id == SUPER_ADMIN_ID:
        buttons.append(["📊 Haftalik hisobot"])
    if user_id == SUPER_ADMIN_ID:
        buttons.append(["Admin qo'shish", "O'quvchi qo'shish"])
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)

def get_rooms_inline():
    rooms = get_all_rooms()
    keyboard = []
    row = []
    for r_id, r_num in rooms:
        row.append(InlineKeyboardButton(str(r_num), callback_data=f"room_{r_id}"))
        if len(row) == 4:
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)
    return InlineKeyboardMarkup(keyboard)

def get_students_inline(room_id):
    students = get_students_by_room(room_id)
    keyboard = []
    for s_id, name, surname in students:
        keyboard.append([InlineKeyboardButton(f"{name} {surname}", callback_data=f"student_{s_id}")])
    keyboard.append([InlineKeyboardButton("⬅️ Orqaga", callback_data="back_rooms")])
    return InlineKeyboardMarkup(keyboard)