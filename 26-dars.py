# 26 - dars
# Class Architecture & Data Security
# Instance Metodlar
# Class metodlar 
# Static Metodlar
# Abstraksiya
# Enkapsulyatsiya
# Data Hiding: public private va protected
# Getter va Setter metodlar
class Student:
    school_name = 'ABC School'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod # bu class ichidagi o'zgaruvchini funksiya ichida o'zgartirish uchun ishlatiladi
    def change_school(cls, school_name):
        # class_name.class_variable
        cls.school_name = school_name

    # instance method
    def show(self):
        print(self.name, self.age, 'School:', Student.school_name)

jessa = Student('Jessa', 20)
jessa.show()

# change school_name
Student.change_school('XYZ School')
jessa.show()

#Class methodlar factory method yaratish uchun ham ishlatiladi.
#  Factory method - turli xil vaziyatlar uchun class obyektini turlicha argumentlar bilan yaratib qaytaradigan method. 

from datetime import date

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def calculate_age(cls, name, birth_year):
        # calculate age an set it as a age
        # return new object
        return cls(name, date.today().year - birth_year)

    def show(self):
        print(self.name + "'s age is: " + str(self.age))

jessa = Student('Jessa', 20)
jessa.show()

# create new object using the factory method
joy = Student.calculate_age("Joy", 1995)
joy.show()

#Statik metodlar class ga tegishli bo’lib, u class yoki obyekt o’zgaruvchilarini ishlatmaydi.

class Employee:
    @staticmethod
    def sample(x):
        print('Inside static method', x)

# call static method
Employee.sample(10)

# can be called using object
emp = Employee()
emp.sample(10)

# Ba'zan obyekt ishlatmaydigan lekin classga tegishli bolgan dastur yozamiz
class Employee(object):

    def __init__(self, name, salary, project_name):
        self.name = name
        self.salary = salary
        self.project_name = project_name

    @staticmethod
    def gather_requirement(project_name):
        if project_name == 'ABC Project':
            requirement = ['task_1', 'task_2', 'task_3']
        else:
            requirement = ['task_1']
        return requirement

    # instance method
    def work(self):
        # call static method from instance method
        requirement = self.gather_requirement(self.project_name)
        for task in requirement:
            print('Completed', task)

emp = Employee('Kelly', 12000, 'ABC Project')
emp.work()

# Static method ni boshqa methoddan chaqirish mumkin

class Test :
    @staticmethod
    def static_method_1():
        print('static method 1')

    @staticmethod
    def static_method_2() :
        Test.static_method_1()

    @classmethod
    def class_method_1(cls) :
        cls.static_method_2()

# call class method
Test.class_method_1()

# Encapsulyatsiya
#Encapsulation dan foydalanib obyektning ichki ko’rinishini, ma’lumotlarini yashira olamiz:

class Employee:
    # constructor
    def __init__(self, name, salary, project):
        # data members
        self.name = name
        self.salary = salary
        self.project = project

    # method
    # to display employee's details
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.salary)

    # method
    def work(self):
        print(self.name, 'is working on', self.project)

# creating object of a class
emp = Employee('Jessa', 8000, 'NLP')

# calling public method of the class
emp.show()
emp.work()

class Employee:
    def __init__(self,name,salary):
        self.name = name # public
        self._project = project # protected
        self.__salary = salary # private

# Public Member

class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data members
        self.name = name
        self.salary = salary

    # public instance methods
    def show(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.salary)

# creating object of a class
emp = Employee('Jessa', 10000)

# accessing public data members
print("Name: ", emp.name, 'Salary:', emp.salary)

# calling public method of the class
emp.show()

# Output:
# Name:  Jessa Salary: 10000
# Name:  Jessa Salary: 10000

# Private Member
# Variable ni faqat class ichida ishlatilishi uchun 
#  uni e’lon qilayotganda nomi oldidan double underscore qo’yamiz: __salary

class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

# creating object of a class
emp = Employee('Jessa', 10000)
# accessing private data members
print('Salary:', emp.__salary)

# # Output:
# Traceback (most recent call last):
#   File "script.py", line 13, in <module>
#     print('Salary:', emp.__salary)
# AttributeError: 'Employee' object has no attribute '__salary'

# Private memberdan tashqarida foydalanishning 2 usuli bor:

# 1) private memberga murojaat qiladigan maxsus public metod yaratish
# 2) name mangling dan foydalanish 

# 1.public metod yaratish:

class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

    # public instance methods
    def show(self):
        # private members are accessible from a class
        print("Name: ", self.name, 'Salary:', self.__salary)

# creating object of a class
emp = Employee('Jessa', 10000)

# calling public method of the class
emp.show()

# Output:
# Name:  Jessa Salary: 10000

# Name mangling - bu usul orqali quyidagi sintaksisdan foydalanib public va protected memberlarga
#  to’g’ridan to’g’ri murojaat qila olamiz: 
# ObyektNomi._ClassNomi.__PrivateMemberNomi
class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

# creating object of a class
emp = Employee('Jessa', 10000)

print('Name:', emp.name)
# direct access to private member using name mangling
print('Salary:', emp._Employee__salary)

# Output: jessa
# Salary: 10000
# protected Member
# Variable ni class va undan voris olgan class lar ishlatilishi uchun 
# uni e’lon qilayotganda nomi oldidan underscore qo’yamiz: _salary

# base class
class Company:
    def __init__(self):
        # Protected member
        self._project = "NLP"

# child class
class Employee(Company):
    def __init__(self, name):
        self.name = name
        Company.__init__(self)

    def show(self):
        print("Employee name :", self.name)
        # Accessing protected member in child class
        print("Working on project :", self._project)

c = Employee("Jessa")
c.show()

# Direct access protected data member
print('Project:', c._project)

# Output
# Employee name : Jessa
# Working on project : NLP
# Project: NLP

# Getter va Setter metodlar
# Inkapsulatsiyadan samarali foydalanish uchun biz 
# getter va setter metodlardan foydalanishimiz kerak.
# Getter metodlarni data member ga murojaat qilish uchun,
#  setter metodlarni esa data memberlarni o’zgartirish uchun ishlatamiz. 
# Odatda getter va setterlar 2ta maqsadda ishlatiladi:
# 1 - private variable larga to’g’ridan-to’g’ri murojaat qilishdan qochish uchun
# 2 - Data mamber uchun validatsiya logikasini qo’shish uchun 

# private variable larga to’g’ridan-to’g’ri murojaat qilishdan qochish uchun
class Student:
    def __init__(self, name, age):
        
        self.name = name # public member
        self.__age = age # private member

    # getter method
    def get_age(self):
        return self.__age

    # setter method
    def set_age(self, age):
        self.__age = age

stud = Student('Jessa', 14)

# retrieving age using getter
print('Name:', stud.name, stud.get_age())

# changing age using setter
stud.set_age(16)

# retrieving age using getter
print('Name:', stud.name, stud.get_age())

# Output:
# Name: Jessa 14
# Name: Jessa 16

# Validatsiya qo’shish uchun ishlatilishi:

class Student:
    def __init__(self, name, roll_no, age):
        # private member
        self.name = name
        # private members to restrict access
        # avoid direct data modification
        self.__roll_no = roll_no
        self.__age = age

    def show(self):
        print('Student Details:', self.name, self.__roll_no)

    # getter methods
    def get_roll_no(self):
        return self.__roll_no

    # setter method to modify data member
    # condition to allow data modification with rules
    def set_roll_no(self, number):
        if number > 50:
            print('Invalid roll no. Please set correct roll number')
        else:
            self.__roll_no = number

jessa = Student('Jessa', 10, 15)

# before Modify
jessa.show()
# changing roll number using setter
jessa.set_roll_no(120)


jessa.set_roll_no(25)
jessa.show()
# Output:
# Student Details: Jessa 10
# Invalid roll no. Please set correct roll number
# Student Details: Jessa 25

# Uyga vazifa
# 1
class BankAccount:
    def __init__(self, balance=0):
        # Initialize the balance attribute
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance}")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")
        return self.balance

# --- Example Usage ---
my_account = BankAccount(100)  # Start with $100
my_account.deposit(50)         # Deposits $50
my_account.withdraw(30)        # Withdraws $30
my_account.check_balance()     # Displays $120

# 2
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def is_square(self):
        # 1. Print the area and perimeter as requested
        print('Area: ', self.area())
        print('Perimeter: ', self.perimeter())
        
        # 2. Check if it is actually a square
        if self.length == self.width:
            print("Is it a square? Yes")
            return True
        else:
            print("Is it a square? No")
            return False
# --- Example Usage ---
rect = Rectangle(10,13)
reac.area()
reac.perimeter

# 3
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self,grade):
        self.grades.append(grade)

    def calculate_average(self):
        if not self.grades: 
            return 0
        return sum(self.grades) / len(self.grades)

    def summary(self):
        average = self.calculate_average()
        print(f"Ism: {self.name}, Yosh: {self.age}")
        print(f"Baholar: {self.grades}")
        print(f"O'rtacha: {average}")
# --- Example Usage ---
talaba = Student("Ali", 20)
talaba.add_grade(85)
talaba.add_grade(95)
talaba.add_grade(75)

talaba.summary

# 4
class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        area = 3.14 * (self.radius ** 2)
    
    def circumference(self):
        circumference = 2 * 3.14 * self.radius 
    
    def diameter(self):
        diameter = self.redius * 2

# --- Example Usage ---
aylana = Circle(10)
aylana.area()
aylana.circumference()
aylana.diameter()

# 5
class Book:
    def __init__(self,title,author,current_page):
        self.title = title
        self.author = author
        self.current_page = current_page

    def open(self):
        print(self.current_page)
    
    def turn_page(self):
        self.current_page += 1
    
    def restart(self):
        self.current_page = 1

# --- Example usage ---    
kitob = Book('Garri Potter','Joanna Roling',330)
kitob.open()
kitob.turn_page()
kitob.restart()

# 6
class Dog:
    total_dogs = 0

    def __init__(self, name):
        self.name = name
        Dog.total_dogs += 1

    @classmethod
    def get_total_dogs(cls):
        return cls.total_dogs

# 7
class Computer:
    total_computers = 0
    computers_list = []

    def __init__(self, brand):
        self.brand = brand
        self.add_computer()

    def add_computer(self):
        Computer.computers_list.append(self.brand)
        Computer.total_computers += 1

# 8
class Employee:
    total_employees = 0
    employees_list = []

    def __init__(self, name):
        self.name = name
        self.hire_employee()

    def hire_employee(self):
        Employee.employees_list.append(self.name)
        Employee.total_employees += 1

# 9
class Television:
    total_televisions = 0
    total_inches = 0
    average_screen_size = 0

    def __init__(self, size):
        self.size = size
        Television.total_televisions += 1
        Television.total_inches += size
        self.update_average_screen_size()

    @classmethod
    def update_average_screen_size(cls):
        if cls.total_televisions > 0:
            cls.average_screen_size = cls.total_inches / cls.total_televisions

# 10
class Course:
    total_courses = 0
    courses_list = []

    def __init__(self, title):
        self.title = title
        self.add_course()

    def add_course(self):
        Course.courses_list.append(self.title)
        Course.total_courses += 1

# 11
class Math:
    @staticmethod
    def multiply(a, b):
        return a * b

# 12
class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

# 13
class Distance:
    @staticmethod
    def miles_to_kilometers(miles):
        return miles * 1.60934

# 14
class Utility:
    @staticmethod
    def is_even(number):
        return number % 2 == 0

# 15. Time klassi - sekunddan minutga
class Time:
    @staticmethod
    def seconds_to_minutes(seconds):
        minutes = seconds // 60
        remaining_seconds = seconds % 60
        return (minutes, remaining_seconds)


# --- Example Usage (Tekshirish uchun) ---

d1 = Dog("Rex")
d2 = Dog("Oktosh")
print(f"6. Jami itlar: {Dog.get_total_dogs()}")

c1 = Computer("Asus")
print(f"7. Kompyuterlar soni: {Computer.total_computers}")

emp1 = Employee("Anvar")
print(f"8. Xodimlar ro'yxati: {Employee.employees_list}")

tv1 = Television(32)
tv2 = Television(50)
print(f"9. O'rtacha TV o'lchami: {Television.average_screen_size}")

course1 = Course("Matematika")
print(f"10. Jami kurslar: {Course.total_courses}")

# Static Methods tekshiruvi
print(f"11. Ko'paytma: {Math.multiply(10, 5)}")
print(f"12. Farengeyt: {Temperature.celsius_to_fahrenheit(25)}")
print(f"13. Kilometr: {Distance.miles_to_kilometers(5)}")
print(f"14. 10 juftmi? {Utility.is_even(10)}")
print(f"15. Vaqt: {Time.seconds_to_minutes(130)}")