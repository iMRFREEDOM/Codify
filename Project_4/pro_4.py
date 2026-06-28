import sqlite3

conn = sqlite3.connect("pro_4.db")
cur = conn.cursor()

# Jadvallarni yaratish
cur.execute("""
CREATE TABLE IF NOT EXISTS accounts( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    balance REAL NOT NULL
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS transactions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    from_account_id INTEGER,
    to_account_id INTEGER,
    amount REAL NOT NULL,
    FOREIGN KEY (from_account_id) REFERENCES accounts(id),
    FOREIGN KEY (to_account_id) REFERENCES accounts(id)
);
""")

# 1. Add user
def add_user():
    print('\n--- Add new user ---')
    name = input('User\'s name: ').upper()
    start_balance = float(input("Starter Balance: "))
    if start_balance < 0:
        print('Starter balance cannot be below 0')
        return
    cur.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", (name, start_balance))
    print("User added successfully")
    conn.commit()

# 2. Display
def display():
    print('\n--- Here is the users list ---') 
    cur.execute("""SELECT * FROM accounts""")
    users = cur.fetchall()
    if not users:
        print("Foydalanuvchilar mavjud emas.")
        return
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, Balance: {user[2]}")

# 3. Deposit
def deposit():
    print('\n / ---- Deposit ---- / ')
    account_id = int(input("Enter your ID: "))
    amount = float(input("Amount: "))
    cur.execute("UPDATE accounts SET balance = balance + ? WHERE id = ?", (amount, account_id))
    print("Deposit completed successfully!")
    conn.commit()

# 4. Withdraw
def withdraw():
    print('\n / ---- Withdraw ---- / ')
    withdraw_account_id = int(input("Enter your ID: "))
    withdraw_amount = float(input("Amount: "))
    
    # TO'G'RILANDI: users emas accounts jadvallari ishlatildi
    query = "SELECT balance FROM accounts WHERE id=?"
    result = cur.execute(query, (withdraw_account_id,)).fetchone()
    
    if result is None:
        print("User not found!")
        return
        
    current_balance = result[0]
    if current_balance < withdraw_amount:
        print('Insufficient amount in balance')
        print(f"Your current balance: {current_balance}")
        return
        
    # TO'G'RILANDI: Balansni kamaytirish va saqlash qo'shildi
    cur.execute("UPDATE accounts SET balance = balance - ? WHERE id = ?", (withdraw_amount, withdraw_account_id))
    conn.commit()
    print("Withdraw completed successfully!")

# 5. Transfer
def transfer():
    print('\n / ---- Transfer ---- / ')
    transfer_from_id = int(input("From who(ID): "))
    transfer_to_id = int(input("To who(ID): "))
    transfer_amount = float(input("Transfer amount: "))
     
    if transfer_from_id == transfer_to_id:
        print('You can\'t transfer to the same account')
        return
        
    # TO'G'RILANDI: accounts jadvalidan qidirish
    query = "SELECT balance FROM accounts WHERE id=?"
    from_user = cur.execute(query, (transfer_from_id,)).fetchone()
    to_user = cur.execute(query, (transfer_to_id,)).fetchone()

    if from_user is None or to_user is None:
        print('One or both accounts not found!')
        return

    current_balance = from_user[0]
    if current_balance < transfer_amount:
        print('Insufficient balance')
        return

    cur.execute("UPDATE accounts SET balance = balance - ? WHERE id = ?", (transfer_amount, transfer_from_id))
    cur.execute("UPDATE accounts SET balance = balance + ? WHERE id = ?", (transfer_amount, transfer_to_id))
    print("Transfer completed successfully!")
    conn.commit()

# 7.To clear all data
# def clear_all_data():
#     print('\n--- Clear All Data ---')
#     confirm = input("Do you really want to clear all? (yes/no): ").lower()
#     if confirm == 'yes':
#         cur.execute("DELETE FROM transactions")
#         cur.execute("DELETE FROM accounts")
#         try:
#             cur.execute("DELETE FROM sqlite_sequence WHERE name='accounts'")
#             cur.execute("DELETE FROM sqlite_sequence WHERE name='transactions'")
#         except sqlite3.OperationalError:
#             pass  
#         conn.commit()
#         print("Data is cleared")
#     else:
#         print("Deleting is canceled.")

# Quit
def quit_program():
    print('The program is closed. Goodbye!')
    conn.close()
    exit()

while True:
    print('\n / -- Main Menu -- / ')
    print(' 1. Add user')
    print(' 2. Display users')
    print(' 3. Deposit')
    print(' 4. Withdraw')
    print(' 5. Transfer')
    # print(' 7. Clear all data')
    print(' 6. Quit')

    choice = int(input("\nChoose the action: "))

    if choice == 1:
        add_user()
    elif choice == 2:
        display()
    elif choice == 3:
        deposit()
    elif choice == 4:
        withdraw()
    elif choice == 5:
        transfer()
    elif choice == 7:
        clear_all_data()
    elif choice == 6:
        quit_program()
    # elif choice == 7:
    #     clear_all_data()
    else:
        print('Invalid choice. Please try again.')
