# insert qilish uchun
# [Table nomi].objects.create([insert qilinadigan qiymatlar])

# upadet qilish uchun 
# 1-usul
# a = [Table nomi].objects.get() - kerakli qiymatni olamiz misol uchun age deylik 
# a.age = [yangi qiymat]
# a.save()

# 2 -usul
# [Table nomi].objects.update(age=F('age')*1.5) {misol uchun 1.5 ga ko'paytirilgani}

# Delete qilish
# [Table nomi].objects.all().delete()
# hamma narsani o'chirib yuboradi

# Miniman
# from django.db.models import Min
# Person.objects.all().aggregate(Min('age'))
# {'age_min':0}

# AVG SUM MAX COUNT hammasi deyarli bir xil ishlaydi
# tepadagi funksiyani MIn degan qismini o'zimizga kerakli amal bilan ishlatsak bo'ladi

# Group by

# [Table nomi].objectives.values('gender').annotate(count=Count('gender'))

# Annotate bu yangi ustun yaratish bo'ladi
