✅ 32 - dars
✅ Relatsion Modellashtirish
✅ Having
✅ Relationships
✅ OneToOne
✅ OneToMany
✅ ManyToMany

# Group by
```sql
SELECT job_id, COUNT(*) FROM employees
GROUP BY job_id;  
 ```
Agar biz COUNT degan ustunni nomini almashtirmoqchi bolsak COUNT(*). as [ustun nomini qoyamiz] deb yozamiz.
hamda WHERE ni qo'shish uchun 
```sql
SELECT job_id, COUNT(*) as hodim_soni FROM employees
WHERE salary > 11000
GROUP BY job_id;  
 ```
# Having
Lekin WHERE juda kuchsiz chunki u o'zi boshqa statement shuning uchun biz Having ishlatamiz
```sql
SELECT job_id, COUNT(*) as xodim_soni FROM employees
GROUP BY job_id
HAVING xodim_soni > 3
``` 
HAVING ni WHEREdan asosiy farqi u GROUP BY bilan birga ishlaydi shuning uchun biz  ... as [psevdonim] qoyganimizni huddi psevdonimidan ishlatishimiz mumkin

# Relationships
SQL da relationships (aloqalar) — bu ikki yoki undan ortiq jadvallar (tables) o‘rtasidagi bog‘liqlikni anglatadi. Ma’lumotlar bazasini to‘g‘ri loyihalash, takrorlanishlarning oldini olish (normalizatsiya) va ma’lumotlar butunligini saqlash uchun aloqalardan foydalaniladi.
# OneToOne
* OneToOne
<br>
bu 1 ga 1 bog'lanish misol uchun 1 odamda faqat 1 ta passport boladi

# OneToMany
* OneToMany
<br>
bu 1 ga kop aloqa bolib misol uchun 1 ta yozuvchining koplab kitoblari bolishi mumkin

# ManyToMany
* ManyToMany
<br>
Bu kopga kop aloqa bolib misol uchun 1 talaba koplab kurslarga borishi mumkin hamda kurslarni hammasi koplab o'quvchilarni oqitishi mumkin