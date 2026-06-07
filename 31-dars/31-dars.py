# 31-dars
# Database so'rovlari
# Order by
# BETWEEN
# IN
# LIKE
# LIMIT
# AVG,SUM,COUNT,MIN,MAX
# UPDATE
# DELETE

# ORDER BY
# ORDER BY bu SQLite da kerakli narsa bo'yicha sort qilib olish uchun ishlatiladi
# SELECT [ kerakli narsalarni tanlab olamiz] FROM [table nomi]
# ORDER BY [nima bo'yicha sortlash],DESC - {kattadan kichikka sort qiladi},{agar maosh bilan sortlaganimizda 2 ta bir xil maosh mavjud boladigan bolsa (misol uchun ismi alifbo tartibi bilan)sortlash}
# DISTINCT - dublikat ma'lumotlarni korsatmaydi

# SELECT [kerakl narsa] FROM [database nomi] WHERE [osha tanlanayotgan narsa] LIKE ['D%'] - Bu yerda LIKE sozidan song menga kerakli narsa blan boshlanishini yozdim
# misol uchun {D} harfida boshlansiz deb % belgisi esa D dan keyin nimadirlar kelsin degani 

# SELECT first_name FROM employees WHERE first_name LIKE '%el';
# bu yerda LIKE dan keyin %(nimadirlar) kelsin keyin el bilan tugasin degan kod boladi bu yerda faqat el bilan tugaydiganlarni olamiz
# % orniga _ belgisi qoyilsa faqat 1 ta belgi kutilayotgan boladi

# SELECT first_name FROM employees WHERE first_name LIKE 'Br__e';
# yuqorida shu faylga faqat Bru__e ismiga tog'ri keladigan odamni qidirayabmiz
# _ belgisini istalgan qismda qoyish mumkin
# SELECT first_name,last_name,hire_date FROM employees WHERE hire_date LIKE '198%';
# Yuqorida men yillar boyicha oldim 

# -- SELECT first_name,last_name,job_id,salary FROM employees
# -- ORDER BY first_name DESC,first_name;

# LIKE
# -- SELECT first_name FROM employees WHERE first_name LIKE 'D%';
# -- SELECT first_name FROM employees WHERE first_name LIKE '%el';
# -- SELECT first_name FROM employees WHERE first_name LIKE 'Br__e';
# -- SELECT first_name,last_name,hire_date FROM employees WHERE hire_date LIKE '198%';

# LIMIT
# -- SELECT first_name,last_name,hire_date FROM employees LIMIT 5;
# LIMIT biror bir jadvalni faqat qaysidir qismini korish uchun ishlatiladi misol uchun 400_000 dan katta jadval bolsa
# men kompyuterni qiynamaslik va vaqtni ketgazmaslik uchun LIMIT ni ishlataman LIMITdan keyin qaysi sonni qoysam o'sha songa teng miqdorda qatorlarni olaman

# -- SELECT first_name,last_name,hire_date FROM employees ORDER BY hire_date LIMIT 5;
# bu yerda ORDER BY nima boyicha ketma ketlashni va osha ketma ketlangan databasedan LIMIT yonidagi son hozirgi holatda beshta ishga eng erta kirgan kishini korsatadi

# OFFSET
# LIMIT berilganda 3 kishini olsa men o'sha uchtadan keyingi 3 tani olish uchun \
# -- SELECT first_name,last_name,hire_date FROM employees ORDER BY hire_date LIMIT 3 OFFSET 3;
#deb yozaman

# BETWEEN
# bu pythonda katta yoki teng deb otirmasdan birdan BETWEEN [qiymat] and [qiymat]
# shu tarzda yoziladi
# quyida misol uchun yozilgan kod
# -- SELECT first_name,last_name FROM employees WHERE salary BETWEEN 6000 and 17000 ORDER BY salary;
# dasturda Maoshi 6000 va 17_000 oralig'idagi ishchilarning ismi va familyasi oylik maoshi osib borish tartibida keltirilgan

# ortacha qiymat olish uchun 
# AVG - average ishlatiladi
# -- SELECT AVG (salary) FROM employees;
# SELECT [bizga kerakli funksiya] FROM [database nomi] 

# yigindi olish uchun
# -- SELECT SUM salary FROM employees;
# SELECT [bizga kerakli funksiya] FROM [database nomi] 

# nechtaligini bilish uchun
# SELECT COUNT (salary) FROM employees;
# SELECT [bizga kerakli funksiya] FROM [database nomi] 

# minimumi ni topish
# SELECT MIN (salary) FROM employees;
# SELECT [bizga kerakli funksiya] FROM [database nomi] 


# maxsimumni topish
# SELECT MAX (min) FROM employees;
# SELECT [bizga kerakli funksiya] FROM [database nomi] 

# UPDATE
# bu biz table larni qaysidir ustunni qiymatini o'zgartirish
# Update ishlaganda korinmaydi chunki SELECT qilinmaydi
# misol uchun familyasi King bolgan odamni oylik maoshini 30_000 ga teng qilib qoymoqchimiz
# UPDATE  employees 
# SET salary = 30_000 
# WHERE 
#   last_name = 'King';

# DELETE ham huddi shunday ishlaydi faqat o'chiradi