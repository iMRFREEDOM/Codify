# 22-dars
# Try Except
x = 6 
try:
  print(x)
except:
  print("An exception occurred")



try:
  print(x)
except NameError:
  print("Variable x is not defined") # agar NameEror xatoligi qaytsa shu except ishlaydi yoqsa keyingisi
except:
  print("Something else went wrong") # biz birdan 2 ta except berishimiz mumkin



try:
  print("Hello")
except:
  print("Something went wrong") # agar xatolik chiqsa shuni qaytaradi
else:
  print("Nothing went wrong") # yoqsa buni



try:
  print(x)
except:
  print("Something went wrong")
finally: # finally xatolik bolsa ham bolmasa ham ishlaydi 
  print("The 'try except' is finished") # bu bizga jarayon tugaganini tushunishga yordam beradi




age = -1

if x < 0:
  raise Exception("Sorry, no ages below zero") # O'zimiz hatolik atayin chiqarish uchun ishlatiladi



x = "hello"

if not type(x) is int: # agar int bolmasa hatolik bersin
  raise TypeError("Only integers are allowed")
