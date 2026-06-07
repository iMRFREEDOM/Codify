# 30 - dars
# Database
# SQL & NoSQL
# RDBMS
# SQLite
# CREATE table - Jadval yaratish
# INSERT
# SELECT
# WHERE
# SQL - (Structured Query Language) - Strukturalashgan so'rovlar tili.
# ushbu til orqali foydalanuvchilar ma'lumotlar omborini boshqarishlari mumkin.
# RDBMS - Relatsion ma'lumotlar bazasi.

# SQLite da dastur boshqacha yozilar
# misol uchun yaratilgan tabledan biror narsani olmoqchi bolsak
# SELECT [olmoqchi bolgan narsamiz nomi] FROM [table nomi]
# agar if sharti qoshmoqchi bolsak
# SELECT [olmoqchi bolgan narsamiz nomi] FROM [table nomi] WHERE [shart misol uchun age<20]
# agar table dan hamma narsani birdan olmoqchi bolsak
# SELECT * FROM [table nomi]
# ya'ni [  *  ] belgisini qoyamiz bu bizga mavjud bolgan hamma narsani olishga yordam beradi

# SELECT name FROM CLIENTS WHERE age=19;
# bunday qilganimizda yoshi 19 ga teng bolgan shaxsni faqat ismini qaytaradi

# Uyga vazifa

# Quyidagi kodlarning barchasi DB Browser for SQLite da yozilgan
## 1 ##
# INSERT INTO City (id, city, country, postalcode)
# VALUES 
#   (0, 'Istanbul', 'Turkiya', 34110),
#   (1, 'Kattaqo''rg''on', 'O''zbekiston', 148000),
#   (2, 'Samarqand', 'O''zbekiston', 140000),
#   (3, 'Tokio', 'Yaponiya', 100),
#   (4, 'Parij', 'Fransiya', 75001),
#   (7, 'Dubay', 'BAA', 0),
#   (8, 'Seul', 'Janubiy Koreya', 189000),
#   (9, 'Wonder', 'Wonderland', 890809),
#   (10, 'Shahar', 'Davlat', 1002),
#   (11, 'shaharcha', 'davlatcha', 2003)

# ;
## 2 ##
# -- INSERT INTO Books (id, name, author, category, price)
# -- VALUES
# -- 	(1, 'Harry Potter', 'Joanna', 'Fantasy', 20),
# -- 	(2, 'kitobikki', 'yozuvchiikki', 'fantasy', 23),
# -- 	(3, 'kitobuch', 'yozuvuch', 'fantasy', 50),
# -- 	(4, 'kitobtor', 'yozuvtor', 'fantasy', 54),
# -- 	(5, 'kitobesh', 'yozuvbesh', 'fantasy', 60),
# -- 	(6, 'kitobolti', 'yozuvolti', 'fantasy', 22),
# -- 	(7, 'kitobyetti', 'yozuvyetti', 'fantasy', 59),
# -- 	(8, 'kitosakkiz', 'yozuvsakkiz', 'fantasy', 80),
# -- 	(9, 'kitotoqqiz', 'yozuvtoqqiz', 'fantasy', 70),
# -- 	(10, 'kitoon', 'yozuvon', 'fantasy', 100);

# SELECT * FROM Books;

## 3 ##
# INSERT INTO User (id, first_name, last_name, age)
# VALUES
# 	(1, 'Harry Potter', 'Joanna', 20),
# 	(2, 'kitobikki', 'yozuvchiikki', 23),
# 	(3, 'kitobuch', 'yozuvuch', 50),
# 	(4, 'kitobtor', 'yozuvtor', 54),
# 	(5, 'kitobesh', 'yozuvbesh', 60),
# 	(6, 'kitobolti', 'yozuvolti', 22),
# 	(7, 'kitobyetti', 'yozuvyetti', 59),
# 	(8, 'kitosakkiz', 'yozuvsakkiz', 80),
# 	(9, 'kitotoqqiz', 'yozuvtoqqiz', 70),
# 	(10, 'kitoon', 'yozuvon', 25);

# SELECT * FROM User WHERE age = 25;
# SELECT first_name, age FROM User WHERE age = 25;
# SELECT * FROM User WHERE id = 3;