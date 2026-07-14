from telegram import ReplyKeyboardMarkup

def get_main_keyboard(user_id, is_admin, super_admin_id):
    # Hamma uchun umumiy tugmalar (1-qator)
    buttons = [
        ["Xonalarni ko'rish", "Anonim fikrlar"]
    ]

    if is_admin or user_id == super_admin_id:
        buttons.append(["📊 Haftalik hisobot", "Baholar kiritish"])
        buttons.append(["Xonalar qo'shish", "O'quvchi qo'shish"])

    if user_id == super_admin_id:
        buttons.append(["Admin qo'shish"])
        
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)