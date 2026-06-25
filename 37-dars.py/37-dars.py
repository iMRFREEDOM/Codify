import sqlite3

conn = sqlite3.connect("sample-database copy.db")
cur = conn.cursor()

cur.execute("""
SELECT * FROM employees LIMIT 3
""")
ans = cur.fetchall()
print(ans[0][1])

cur.close()
conn.close()