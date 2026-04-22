# 25 - dars OOP - davomi
# konstruktor destruktor vorisdorlik polimorfizm
# dunder metod - __xxxx__ 2 ta _ bilan yoziladigan narsa
# Konstruktorlar 3 xil boladi
# 1.Default
# 2.Non-Parametrised def __init__(self):
# Parametrized def __init__(self,v1,v2,v3....)
# Default class:
class Employee:

    def display(self):
        print('Inside Display')
    
emp = Employee()
emp.display()
# Non-parametred class:
class Company:

    def __init__(self):
        self.name = 'PYnative'
        self.address = "ABC Street"

    def show(self):
        print('Name:',self.name, 'Address:', self.address)
cmp = Company()
cmp.show()
# Parametred class:
class Ishchi:

    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def show(self):
        print(self.name , self.age , self.salary)
    
emma = Ishchi('Emma',23,7500)
emma.show()

kelly = Ishchi('Kelly',25,8500)
kelly.show()
# KONSTRUKTOR __init__ BILAN YOZILADI
class Employee:
    count = 0
    def __init__(self):
        Employee.count = Employee.count + 1


# creating objects
e1 = Employee()
e2 = Employee()
e3 = Employee()
print("The number of Employee:", Employee.count)

####
# Destructor
class Student:

    # constructor
    def __init__(self, name):
        print('Inside Constructor')
        self.name = name
        print('Object initialized')

    def show(self):
        print('Hello, my name is', self.name)

    # destructor
    def __del__(self):
        print('Inside destructor')
        print('Object destroyed')

# create object
s1 = Student('Emma')
s1.show()

# delete object
del s1


# OUTPUT
# Inside Constructor
# Object initialized

# Hello, my name is Emma

# Inside destructor
# Object destroyed

# destructor agar reference count 0 ga teng bolsa garbage collection uni o'chiriadi
######################################################################
# Vorisdorlik va Polimorfizm
class Odam: # Parent class
    oyoqlar_soni = 2
    qollar_soni = 2

     # Hozirda Jangchi klassini  ichida Odam klassidagi o'zgaruvchilar hammasi bor
class Jangchi(Odam): # Child Class
    energiya = 100
    jang_qiyinligi = 30

    def jang_qil(self):
        if self.energiya > self.jang_qiyinligi:
            self.energiya -= self.jang_qiyinligi
            print(f'Jangda {self.jang_qiyinligi} energiya yo\'qotildi, {self.energiya} qoldi')
        else:
            print('Jang uchun energiya yetmadi')

Botir = Jangchi()
Botir.jang_qil() # 70 qoldi
Botir.jang_qil() # 40 qoldi
Botir.jang_qil() # 10 qoldi
Botir.jang_qil() # yetarli emas

# Uyga vazifa
class Texnika:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Turi: {self.type}")

texnik = Texnika('Samsung', 'S23 Ultra', 'Smartphone' )
texnik.info()

class Notebooks(Texnika):
    def __init__(self, brand, model, type, video_card, ram, display):
        super().__init__(brand, model, type)
        self.video_card = video_card
        self.ram = ram
        self.display = display

    def more_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Turi: {self.type}, "
              f"Video karta: {self.video_card}, RAM: {self.ram}, Displey: {self.display}")
        
note = Notebooks('Victus','ideapad','Noutebook','RTX 5090' , '16GB', 'Ultra HD')
note.more_info()


class Televisions(Texnika):
    def __init__(self, brand, model, type, size, display):
        super().__init__(brand, model, type)
        self.size = size
        self.display = display

    def more_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Turi: {self.type}, "
              f"O'lchami: {self.size}, Displey: {self.display}")

tele = Televisions('Samsung','SmartTV','Televizor','55','Ultra 8K')
tele.more_info()

class Smartphones(Texnika):
    def __init__(self, brand, model, type, size, sim_count):
        super().__init__(brand, model, type)
        self.size = size
        self.sim_count = sim_count
    
    def more_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Turi: {self.type}, "
              f"O'lchami: {self.size}, SIM-kartalar soni: {self.sim_count}")

smartphones = Smartphones('Samsung','J4','Smartphone','30cm',2)
smartphones.more_info()


###################################### 2 - Topshiriq ############################################


class Transport:
    def __init__(self,brand ,model,type):
        self.brand = brand
        self.model = model
        self.type = type
    
    def info(self):
        print(f"Brend:{self.brand},Model:{self.model},Type:{self.type}")

trans = Transport('KIA' , 'K5' , 'Yengil')
trans.info()

class ElectroCars(Transport):
    def __init__(self,brand,model,type,battery_life,chargin_time):
        super().__init__(brand,model,type)
        self.battery_life = battery_life
        self.chargin_time = chargin_time

    def more_info(self):
        print(f"Brend:{self.brand},Model:{self.model},Type:{self.type},Battery life:{self.battery_life},Charging time:{self.chargin_time}")

electro = ElectroCars('Tesla','Cybertruck','Yengil','3 yil','2 hours')
electro.more_info()

class SportCars(Transport):
    def __init__(self,brand,model,type,motor,color):
        super().__init__(brand,model,type)
        self.motor = motor
        self.color = color
    
    def more_info(self):
        print(f"Brend:{self.brand},Model:{self.model},Type:{self.type},Motor:{self.motor},Color:{self.color}")

sport = SportCars('Porsche',911,'Yengil','340 horse power','Black')
sport.more_info()

class Truck(Transport):
    def __init__(self,brand,model,type,motor, height, long, weight):
        super().__init__(brand,model,type)
        self.motor = motor
        self.height = height
        self.long = long
        self.weight = weight

    def more_info(self):
        print(f"Brend:{self.brand},Model:{self.model},Type:{self.type},Height:{self.height},Long:{self.long},Weight:{self.weight}")

truck = Truck('MAN','Volvo','Heavy','500 hp',7,20,5000)
truck.more_info()

###################################### 3 - Topshiriq ############################################

class University:
    def __init__(self, university):
        self.university = university

    def info(self):
        print(f"University: {self.university}")



class Staff(University):
    def __init__(self, university, first_name, last_name, age):
        super().__init__(university)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def staff_info(self):
        print(f"University: {self.university}, Name: {self.first_name} {self.last_name}, Age: {self.age}")



class Student(Staff):
    def __init__(self, university, first_name, last_name, age, group):
        super().__init__(university, first_name, last_name, age)
        self.group = group
    
    def more_info(self):
        print(f"University: {self.university}, Student: {self.first_name} {self.last_name}, Age: {self.age}, Group: {self.group}")



class Teacher(Staff):
    def __init__(self, university, first_name, last_name, age, position, subject):
        super().__init__(university, first_name, last_name, age)
        self.position = position
        self.subject = subject
    
    def more_info(self):
        print(f"University: {self.university}, Teacher: {self.first_name} {self.last_name}, Position: {self.position}, Subject: {self.subject}")



class OtherStaff(Staff):
    def __init__(self, university, first_name, last_name, age, position):
        super().__init__(university, first_name, last_name, age)
        self.position = position
    
    def more_info(self):
        print(f"University: {self.university}, Staff: {self.first_name} {self.last_name}, Position: {self.position}")



class Object(University):
    def __init__(self, university, name):
        super().__init__(university)
        self.name = name
    
    def object_info(self):
        print(f"University: {self.university}, Object Name: {self.name}")



class Computer(Object):
    def __init__(self, university, name, soni, tizimi, holati):
        super().__init__(university, name)
        self.soni = soni
        self.tizimi = tizimi
        self.holati = holati
    
    def object_more_info(self):
        print(f"University: {self.university}, Name: {self.name}, Qty: {self.soni}, OS: {self.tizimi}, Status: {self.holati}")



class Mebel(Object):
    def __init__(self, university, name, soni, turi, holati):
        super().__init__(university, name)
        self.soni = soni
        self.turi = turi
        self.holati = holati
    
    def object_more_info(self):
        print(f"University: {self.university}, Name: {self.name}, Qty: {self.soni}, Type: {self.turi}, Status: {self.holati}")



print("--- 3.1 Natijalari ---")
student = Student('Cambridge', 'Tom', 'Cruise', 25, 'Group-119')
student.more_info()


teacher = Teacher('Oxford', 'Alan', 'Turing', 45, 'Professor', 'Mathematics')
teacher.more_info()


print("\n--- 3.2 Natijalari ---")
comp = Computer('TUIT', 'HP Victus', 20, 'Windows 11', 'Yangi')
comp.object_more_info()


mebel = Mebel('WIUT', 'Parta', 50, 'Yog`ochli', 'O`rtacha')
mebel.object_more_info()
