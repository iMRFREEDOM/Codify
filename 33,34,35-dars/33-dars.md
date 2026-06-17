# 33 - dars
# Jonis
Inner join - bu 2 ta tableni birlashmasini oladi
Uni sintaksisi:
```sql
SELECT <select_lsit>
FROM Table_A A
INNER JOIN Table_B B
ON A.key = B.key
```
Misol uchun:
```sql
SELECT c.country_name, region_name
FROM countries c INNER JOIN Regions r
ON c.region_id = r.region_id;
```
Left join bu 1-table ni hamda 2-table bilan kesishan qismni olib ketadi
Right join bu kesishmani hamda 2-table ni olib ketadi
```sql
SELECT <select_list>
FROM Table_A A
RIGHT JOIN Table_B B
ON A.key = B.key;
```
Full Outer Join
Full outer join - bu ikkala tableni ham barcha ma'lumotlarini oladi. Mos kelmagan barcha joylarga NULL qo'yib chiqadi.
Eslatma: SQLite buni ham to'g'ridan-to'g'ri qo'llab-quvvatlamaydi, o'rniga LEFT JOIN va UNION ishlatiladi.
```sql
SELECT <select_list>
FROM Table_A A
FULL OUTER JOIN Table_B B
ON A.key = B.key;
```
Cross Join
Cross join - bu ulanish shartisiz (ON kalit so'zisiz) ikkala tablening har bir qatorini bir-biriga ko'paytirib chiqadi (Dekart ko'paytma).
```sql
SELECT c.country_name, r.region_name
FROM countries c CROSS JOIN regions r;
```