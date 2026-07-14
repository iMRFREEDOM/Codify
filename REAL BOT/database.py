import sqlite3

def get_connection():
    return sqlite3.connect("bot_database.db")

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Adminlar jadvali
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS admins(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER NOT NULL UNIQUE)""")
   
    # Honalar jadvali
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rooms(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_number INTEGER)""")
  
    # O'quvchilar jadvali
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             student_name TEXT NOT NULL,
             student_surname TEXT NOT NULL,
             room_id INTEGER,
             photo_id TEXT,
             FOREIGN KEY (room_id) REFERENCES rooms(id))""")
   
    # Baholar jadvali
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS grades(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_id INTEGER,
            category TEXT,
            date TEXT,
            score INTEGER,
            FOREIGN KEY (room_id) REFERENCES rooms(id),
            UNIQUE (room_id, date, category))""")
    
    # FEEDBACKLAR jadvali
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedbacks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            feedback_text TEXT NOT NULL,
            created_at TEXT NOT NULL, -- Ma'lumot turi qo'shildi
            reply_text TEXT,
            replied_at TEXT)""")

    conn.commit()
    conn.close()
