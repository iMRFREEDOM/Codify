#decorator - funksiyani argument sifatida olib, uning o’zgartirilgan nusxasini qaytaruvchi funksiya.  
# Decorator bevosita funksiyani o’zgartirmasdan, undan oldin va keyin ishlaydigan kodlar qo’shish 
# imkonini beradi.
def query(friends, *args):
    for f in args:
        def g(*args, **kwargs):
            nonlocal friends
            friends = f(*args, **kwargs)
        return g

def func(x):
    return 2 * x

func = query(func)
func(2)  # Output is 4

#Bunda tashqi funksiya **deco** argument sifatida **f** ni oladi va uning ichidagi **g** funksiya **closure** sifatida e’lon qilinyapti. 
#Biz **func** deb nomlangan funksiya yaratib uni **deco** ga argument qilib beramiz. Hamda **closure** ni ishlatish uchun uni yana **func** deb nomlangan o’zgaruvchiga tenglaymiz. 
#Shunda **deco func** ni **argument** sifatida olyabdi va o’zini **closure** ini yana **func** ga tenglayabdi.
#Bu holda biz **func deco tomonidan decoratsita qilingan** yoki **deco - func ning decoratori** deb aytamiz.

#Biz decoratordan foydalanib funksiyani o’zini o’zgartirmasdan, undan oldin va keyin ishlashi kerak bo’lgan kodlar bilan to’ldira olaimiz.  
def deco(f):
    def g(*args, **kwargs):
        print("by Komiljon ", f.__name__)
        return f(*args, **kwargs)
    return g

def func(x):
    return 2*x

func = deco(func)
func(2)

# 1. Fuksiya qaytaradigan stringni katta harflarga o'tkazib beradigan dekorator yarating.
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


@uppercase_decorator
def greet(name):
    return f"Hello, {name}!"


@uppercase_decorator
def greet2(name):
    return f"bye, {name}!"
#
# result = greet2("John")
# print(result)  # Output: "HELLO, JOHN!"

# 3. Funksiya ishlashi uchun qancha vaqt ketganini hisoblab beradigan dekorator yozing
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.2f} seconds to execute")
        return result
    return wrapper

@timer_decorator
def some_function():
    a = 0
    for i in range(99999999):
        a += 5

# some_function()

# 4. Funksiya necha marta chaqirilganini sanovchi dekorator yozing
def count_calls_decorator(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count_calls_decorator
def some_function():
    a = 0
    for i in range(3):
        a += 1
    return a

f = some_function()
g = some_function()
print(f, g)
print(some_function.calls)



