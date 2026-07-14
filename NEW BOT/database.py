import sqlite3

def get_connection():
    return sqlite3.connect("bot_database.db")

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Adminlar jadvali
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS admins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER NOT NULL UNIQUE
        )
    """)

    # Xonalar jadvali
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rooms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_number INTEGER NOT NULL UNIQUE
        )
    """)

    # O'quvchilar jadvali
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            student_surname TEXT NOT NULL,
            room_id INTEGER,
            photo_id TEXT,
            FOREIGN KEY (room_id) REFERENCES rooms(id)
        )
    """)

    # Baholar jadvali
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS grades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_id INTEGER,
            date TEXT,
            category TEXT,
            score INTEGER,
            FOREIGN KEY (room_id) REFERENCES rooms(id),
            UNIQUE (room_id, date, category)
        )
    """)

    # Feedbacklar jadvali
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedbacks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_id INTEGER,
            feedback_text TEXT NOT NULL,
            created_at TEXT NOT NULL,
            reporter_id INTEGER,
            reply_text TEXT,
            replied_at TEXT,
            FOREIGN KEY (room_id) REFERENCES rooms(id)
        )
    """)
    conn.commit()
    conn.close()
#########################################
def is_admin_in_db(telegram_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM admins WHERE telegram_id = ?", (telegram_id,))
    row = cursor.fetchone()
    conn.close()
    return row is not None
#############################################
def add_admin(telegram_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO admins (telegram_id) VALUES (?)", (telegram_id,))
        conn.commit()
        success = True
    except sqlite3.IntegrityError:
        success = False
    conn.close()
    return success

def get_all_rooms():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, room_number FROM rooms ORDER BY room_number ASC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_room_id_by_number(room_number):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM rooms WHERE room_number = ?", (room_number,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

def get_students_by_room(room_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, student_name, student_surname FROM students WHERE room_id = ?", (room_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_student(name, surname, room_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (student_name, student_surname, room_id) VALUES (?, ?, ?)", (name, surname, room_id))
    conn.commit()
    conn.close()


    
########################################
def save_student_photo(student_id, photo_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET photo_id = ? WHERE id = ?", (photo_id, student_id))
    conn.commit()
    conn.close()
###########################################
def get_student_photo(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT photo_id FROM students WHERE id = ?", (student_id,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None
##################################################
def insert_grade(room_id, date_str, category, score):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO grades (room_id, date, category, score)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(room_id, date, category) DO UPDATE SET score=excluded.score
    """, (room_id, date_str, category, score))
    conn.commit()
    conn.close()
######################################################33
def add_feedback(room_id, text, created_at, reporter_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO feedbacks (room_id, feedback_text, created_at, reporter_id) VALUES (?, ?, ?, ?)",
                   (room_id, text, created_at, reporter_id))
    feedback_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return feedback_id
###########################################3
def get_all_feedbacks(limit=10):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT feedbacks.id, rooms.room_number, feedbacks.feedback_text, feedbacks.created_at, feedbacks.reporter_id, feedbacks.reply_text 
        FROM feedbacks 
        LEFT JOIN rooms ON feedbacks.room_id = rooms.id 
        ORDER BY feedbacks.id DESC LIMIT ?
    """, (limit,))
    rows = cursor.fetchall()
    conn.close()
    return rows
###############################################
def get_feedback_by_id(feedback_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, room_id, feedback_text, created_at, reporter_id, reply_text FROM feedbacks WHERE id = ?", (feedback_id,))
    row = cursor.fetchone()
    conn.close()
    return row
################################################
def set_feedback_reply(feedback_id, reply_text, replied_at):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE feedbacks SET reply_text = ?, replied_at = ? WHERE id = ?", (reply_text, replied_at, feedback_id))
    conn.commit()
    conn.close()
####################################################
def delete_feedback(feedback_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM feedbacks WHERE id = ?", (feedback_id,))
    conn.commit()
    conn.close()
###################################################
if __name__ == "__main__":
    create_tables()
    # Dastlabki xonalarni yaratish (Agar bo'sh bo'lsa)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM rooms")
    if cursor.fetchone()[0] == 0:
        # 2-qavat xonalari
        for r in range(201, 218):
            cursor.execute("INSERT OR IGNORE INTO rooms (room_number) VALUES (?)", (r,))
        # 3-qavat xonalari
        for r in range(301, 318):
            cursor.execute("INSERT OR IGNORE INTO rooms (room_number) VALUES (?)", (r,))
        conn.commit()
    conn.close()
#######################################