# def orm_list(request):
#     countries = Countries.objects.all()
#     country_list = ""
#     for c in countries:
#         country_list += f"<li>{c.country_name}</li>"
#     return HttpResponse(f"<ul>{country_list}</ul>")

# countries = Countries.objects.all()
# o'rniga countries = Countries.objects.only() deb qavs ichiga o'zimizga kerakli ustun nomini yozsak faqat o'sha ustundagi narsalar nomini olib kelib beradi

# agar uni o'rniga filter desak bu SQLite da WHERE dagiga o'xshaydi
# qavs ichiga bizga kerakli shartni yozamiz misol uchun
# countries = Countries.objects.filter(region_id = 2)

# def orm_list(request):
#     countries = Countries.objects.all(country_name__startswith='A') # Bu holda faqat A bilan boshlanadigan larni chaqirayabdi country_name deganda ustun nomi __ va startswith deganda kerakli queryni chaqiriayotgan bo'ladi 
#     country_list = ""
#     for c in countries:
#         country_list += f"<li>{c.country_name}</li>"
#     return HttpResponse(f"<ul>{country_list}</ul>")


# Bularni hammasi queryset deb nomlanadi chunki SQLite dagi querylarni olib beradi va uni Djang tiliga tarjima qiladi

########### Overall
 
# where shartini ORM da targ'im qilish uchun 
# [table nomi].objects.filter([Shart qo'yiladi])

# yoki va degan amallarni bajarish uchun
# & - va | - yoki

# kattaroq demoqchi bo'lsak gt
# kichikroq demoqchi bolsak lt boladi
# gte teng yoki katta