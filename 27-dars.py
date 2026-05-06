# 27 - dars Konspekt
# Pythonda fayllar bilan ishlash
# Pythonda modul va paket
# Fayllar bilan ishlash
# JSON


# from dars_for_27 import Student  # dars_for_27 fayldan Student klassini import qilib birdan ishlatish uchun

# Nodir = Student('Nodir',20)
# print(nodir.name)


#               ---{ Fayllar bilan ishlash }---              # 
print("--------------------------------")
f = open("matn.txt","r")
print(f)
print("--------------------------------")
f = open("matn.txt","r")
print(f.read())
print("--------------------------------")
f = open("matn.txt","r")
print(f.read(6))
print("--------------------------------")
f = open("matn.txt","r")
print(f.readline())
print("--------------------------------") 
f = open("matn.txt","r") # bu faqat o'qish uchun hech nima o'zgartirib bolmaydi
for i in f:
    print(i)
f.close() 
print("--------------------------------")
f = open("matn.txt","a") # eppend ga o'xshaydi
f.write("Endi Faylda yana 1 qator mavjud")
f.close()
print("1 qator qoshildi")
print("--------------------------------")
f = open("matn.txt","w") # oldin nima yozilgan bolsa hammasini o'chirib yangi narsani qayta yozadi
f.close()

#               ---{ JSON }---              # 

# JSON bu backend va frontend chi orasida aloqachi
# Encoding - JSON ga o'tkazish ,Decoding - JSON dan o'tkazish
# baytlar ketma ketligi hamda internet orqali jo'natishga kerak
 