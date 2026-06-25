import sqlite3
from contextlib import closing

def get_connection(database_path):
    return closing(sqlite3.connect(database_path))

# CREATE
def create_employee(database_path, first_name, last_name):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO employees (first_name, last_name) VALUES (?, ?)", (first_name, last_name))
        connection.commit()
        return cursor.lastrowid

# READ
def get_employee(database_path, employee_id):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM employees WHERE id=?", (employee_id,))
        return cursor.fetchone()

# UPDATE
def update_employee(database_path, employee_id, name=None, bio=None):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        if name:
            cursor.execute("UPDATE employees SET name=? WHERE id=?", (name, employee_id))
        if bio:
            cursor.execute("UPDATE employees SET bio=? WHERE id=?", (bio, employee_id))
        connection.commit()

# DELETE
def delete_employee(database_path, employee_id):
    with get_connection(database_path) as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM employees WHERE id=?", (employee_id,))
        connection.commit()