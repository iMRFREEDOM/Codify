import sqlite3

def get_connection():
    return sqlite3.connect("bot_database.db")

def check_is_admin(telegram_id):
   try:
    conn = get_connection()
    cursor = conn.cursor()

    # SQL da telegram id ni olish
    cursor.execute("SELECT 1 FROM admins WHERE telegram_id = ?",(telegram_id))
    
    result = cursor.fetchone()
    conn.close()
    return True
   except sqlite3.IntegrityError:
      return False
   finally:
      conn.close()

def get_all_rooms():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, room_number FROM rooms")
    rooms = cursor.fetchall()
    conn.close()
    return rooms