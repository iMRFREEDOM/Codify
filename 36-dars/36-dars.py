# ```sql
# CREATE TABLE students (
#   id INTEGER PRIMARY KEY,
#   first_name TEXT NOT NULL,
#   last_name TEXT NOT NULL
# );

# CREATE TABLE teachers (
#   id INTEGER PRIMARY KEY,
#   first_name TEXT NOT NULL,
#   last_name TEXT NOT NULL
# );

# -- Insert sample data into the students table
# INSERT INTO students (id, first_name, last_name) VALUES
# (1, 'Alice', 'Adams'),
# (2, 'Bob', 'Baker'),
# (3, 'Carol', 'Carter'),
# (4, 'David', 'Diaz'),
# (5, 'Eva', 'Evans');

# -- Insert sample data into the teachers table
# INSERT INTO teachers (id, first_name, last_name) VALUES
# (1, 'Frank', 'Fisher'),
# (2, 'Grace', 'Griffin'),
# (3, 'Henry', 'Harrison'),
# (4, 'Irene', 'Ingram'),
# (5, 'Jack', 'Andrey');
# INSERT INTO orders (order_id, product, quantity) VALUES
# (1, 'Laptop', 5),
# (2, 'Keyboard', 10),
# (3, 'Mouse', 15),
# (4, 'Monitor', 7),
# (5, 'Printer', 3);

# INSERT INTO shipments (shipment_id, product, quantity) VALUES
# (1, 'Laptop', 5),
# (2, 'Keyboard', 8),
# (3, 'Mouse', 15),
# (4, 'Monitor', 4),
# (5, 'Headphones', 6);```


# Union 2 ta tableni birlashtiradi
# SELECT first_name,last_name
# FROM students
# UNION 
# SELECT irst_name,lst_name
# FROM teachers;

# Union oddiy qilib tushunish uchun 1-tabledan element tanlab 
# union yozib keyin shunchaki 2-tabledan element tanlab qoyish kerak

# Union 2 ta tableni birlashtiradi
# SELECT first_name,last_name
# FROM students
# UNION ALL
# SELECT irst_name,lst_name
# FROM teachers;

# yuqoridagi nisbatan tezroq ishlaydi chunki u duplikat bormi yoqmi qarab otirmaydi shuning uchun duplikarlar paydo bolib qolishi mumkin

# INTERSECT

# UNION + WHERE: Familyasi A bolan boshlanadigan O'quvchi va ustozlarni birlashtirish
# SELECT first_name, last_name
# FROM students
# WHERE last_name LIKE 'A%'
# UNION
# SELECT first_name, last_name
# FROM teachers
# WHERE last_name LIKE 'A%';


# UNION + ORDER BY : Familiya boyicha tartiblaymiz
# SELECT first_name, last_name
# FROM students
# UNION
# SELECT first_name, last_name
# FROM teachers
# ORDER BY last_name;

# UNION + LIMIT
# SELECT first_name, last_name
# FROM (
#   SELECT id, first_name, last_name
#   FROM students
#   ORDER BY id
#   LIMIT 5
# )
# UNION
# SELECT first_name, last_name
# FROM (
#   SELECT id, first_name, last_name
#   FROM teachers
#   ORDER BY id
#   LIMIT 5
# );

# INTERSECT FAQAT 2 SIDA BORINI OLADI ORTIQCHASINI O'CHIRADI

# EXCEPT da faqat 1-royhatda borini oladi


# Uyga vazifa

# 1-topshiriq
"""
SELECT first_name,last_name
FROM students
UNION
SELECT first_name,last_name
FROM teachers
WHERE UPPER(first_name) LIKE 'A%'
	OR UPPER(first_name) LIKE 'E%'
	OR UPPER(first_name) LIKE 'O%'
	OR UPPER(first_name) LIKE 'U%'
	OR UPPER(first_name) LIKE 'I%';
"""
# 2 - topshiriq
"""




"""
# 3 - topshiriq
"""
SELECT first_name, last_name,'Talaba' as manba
FROM students
UNION
SELECT first_name,last_name,'Oqituvchi'  as manba
FROM teachers
ORDER BY manba ASC,last_name ASC;
"""
# 4 - topshiriq
"""
SELECT id, first_name, last_name FROM students
UNION ALL
SELECT id, first_name, last_name FROM teachers
ORDER BY id DESC
LIMIT 3;
"""
# 5 - topshiriq
"""
SELECT quantity 
FROM orders
INTERSECT
SELECT quantity
FROM shipments
"""
# 6 - topshiriq
"""
SELECT quantity 
FROM orders
WHERE quantity >= 5
INTERSECT
SELECT quantity
FROM shipments
WHERE quantity >= 5
"""
# 7 - topshiriq
"""
SELECT orders.order_id
FROM orders, shipments
WHERE orders.product = shipments.product
  AND orders.quantity = shipments.quantity;
"""
# 8 - topshiriq
"""
SELECT shipments.shipment_id
FROM orders, shipments
WHERE orders.product = shipments.product
  AND orders.quantity = shipments.quantity
  ORDER BY orders.product DESC;
"""
# 9 - topshiriq
"""
SELECT product
FROM orders
EXCEPT
SELECT product
FROM shipments
"""
# 10 - topshiriq
"""
SELECT product
FROM shipments
EXCEPT
SELECT product
FROM orders
"""
# 11 - topshiriq
"""
SELECT order_id
FROM orders
WHERE order_id >= 10
EXCEPT
SELECT shipment_id
FROM shipments;
"""
# 12 - topshiriq
"""
SELECT shipment_id, quantity
FROM shipments
WHERE quantity < 5
EXCEPT
SELECT order_id, quantity
FROM orders
ORDER BY quantity DESC;
"""	
