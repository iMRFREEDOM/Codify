# 24-dars
# OOP
# OOP = Object oriented programming - fObyektga yo'naltirilgan dasturlash
# Paradigma - muammoni yechish uchun ma'lum tushuncha va texnologiyalar to'plami
# Biz hamma naesani obyekt sifatida olamiz
# Obyektda 2 ta narsa boladi Qiymat va Harakat
# Obyektni mashina deb olsak
# Qiymat = Rangi, Narxi , Tezligi
# Harakat = Yurish, To'xtash , Signal chalish
# Classni ichida funksiya yaratilsa u obyekt deyiladi
# Class va Obyekt
# Obyektlar - siz his qilishingiz, boshqarishingiz yoki ta’sir qilishingiz mumkin bo’lgan real-hayot subyektlari. 
# Masalan inson:
# Xususiyatlari (**property): ismi, yoshi, jinsi**    va
# Xatti-harakatlari(**behaviors**): yuradi, uxlaydi, yeydi


# Output:
# Doe 20
# Anna 18
###################################################################
# method - classga tegishli bo'lgan funksiya
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def speak(self,word):
        print(f"{self.name} aytadi: {word}")

Doe = Person(name="Doe", age=20, gender="male")
Anna = Person(name="Anna", age=18, gender="female")

Doe.speak("Salom Anna")
Anna.speak("Salom Doe, yaxshimisan?")

# Output:
# Doe aytadi: Salom Anna
# Anna aytadi: Salom Doe, yaxshimisan?

class Person:
    arms = 2
    legs = 2
    country = 'Uzbekistan' #bular klassni o'zgaruvchilari
    # def funksiyasidan tashqaridagi barcha o'zgaruvchilar classga tegishli boladi
    # klass har bir obyekt uchun tepadagi 3 ta o'zgaruvchini umumiy qilib oladi

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def speak(self,word):
        print(f"{self.name} aytadi: {word}")
    
    def change_country(cls, new):
        cls.country = new

Doe = Person(name="Doe", age=20, gender="male")
Anna = Person(name="Anna", age=18, gender="female")

Doe.speak("Salom Anna")
Anna.speak("Salom Doe, yaxshimisan?")
print(Doe.arms)

Doe.change_country('USA')
Anna.country('Russia')

print(Doe.country)
print(Anna.country)
# Output:
# Doe aytadi: Salom Anna
# Anna aytadi: Salom Doe, yaxshimisan?
# 2

# Uyga vazifa
# 1 - vazifa
class Oson1:
    a = 0
    def output_a(self):
        print(self.a)
# 2 - vazifa
class Oson2:
    a = 0
    b = 0
    def summa(self):
        print(self.a + self.b)
# 3 - vazifa
class Oson3:
    a = 0
    def plus_minus(self):
        if self.a > 0:
            print("Musbat")
        elif self.a < 0:
            print("Manfiy")
        else:
            print("0 ga teng")
# 4 - vazifa
class Oson4:
    a = 0
    def odd_even(self):
        if self.a % 2 == 0:
            print("Juft")
        else:
            print("Toq")
# 5 - vazifa
class Oson5:
    a = 0
    b = 0
    def daraja(self):
        print(self.a ** self.b)
# 6-vazifa
class MyClass6:
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def remove(self, word):
        if word in self.words:
            self.words.remove(word)

# 7-vazifa
class MyClass7:
    def __init__(self):
        self.myDict = {}

    def add_elem(self, key, val):
        if key not in self.myDict:
            self.myDict[key] = val

    def update_elem(self, key, val):
        if key in self.myDict:
            self.myDict[key] = val

# 8-vazifa
class MyClass8:
    def __init__(self, numbers):
        self.numbers = numbers

    def compare_lists(self, new_list):
        if sum(self.numbers) > sum(new_list):
            print(self.numbers)
        else:
            print(new_list)

# 9-vazifa
class MyClass9:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def list1_max(self):
        return max(self.list1) if self.list1 else 0

    def list2_max(self):
        return max(self.list2) if self.list2 else 0

    def sum_of_two_max(self):
        total = self.list1_max() + self.list2_max()
        print(total)

# 10-vazifa
class MyClass10:
    def __init__(self, numbers):
        self.numbers = numbers

    def divide(self, d):
        res = [x for x in self.numbers if x % d == 0]
        return res