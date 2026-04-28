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
        
