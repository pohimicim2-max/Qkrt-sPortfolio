
<div align="center">

# Python
### Здесь будут публиковаться основы `Python` и то, что связано с ним.
</div>

---

# №1 - Основы `Python`

### 1. Переменные и типы данных

>[!note]
> ### **Теория:** 
> В `Python` переменная создаётся при первом присваивании значения. Тип данных определяется автоматически.

**Примеры:**
```python
# Простые типы данных
name = "Анна"          # str - строка
age = 25               # int - целое число
price = 19.99          # float - число с плавающей точкой
is_active = True       # bool - логический тип (True/False)

# Коллекции
fruits = ["яблоко", "банан", "апельсин"]        # list - список (изменяемый)
coordinates = (10.5, 20.3)                       # tuple - кортеж (неизменяемый)
unique_numbers = {1, 2, 3, 3}                    # set - множество (уникальные элементы)
person = {"name": "Иван", "age": 30}             # dict - словарь (ключ-значение)
```

### 2. Базовые операторы и операции

>[!note]
>### **Теория:**
> Операторы позволяют выполнять действия с данными: математические, сравнения, логические.

**Примеры:**
```python
# Арифметика
sum = 5 + 3    # 8
diff = 10 - 4  # 6
prod = 6 * 7   # 42
quot = 15 / 4  # 3.75 (деление всегда float)
quot_int = 15 // 4  # 3 (целочисленное деление)
remainder = 15 % 4  # 3 (остаток от деления)
power = 2 ** 3 # 8 (возведение в степень)

# Сравнение
print(5 > 3)   # True
print(5 == 5)  # True
print(5 != 3)  # True

# Логические операторы
print(True and False)  # False
print(True or False)   # True
print(not True)        # False
```

### 3. Управление потоком (Условия)

>[!note]
> ### **Теория:**
> Условные конструкции позволяют выполнять разный код в зависимости от условий.

**Примеры:**
```python
# if/elif/else
score = 85

if score >= 90:
    grade = "5"
elif score >= 75:
    grade = "4"
elif score >= 60:
    grade = "3"
else:
    grade = "2"

print(f"Оценка: {grade}")  # Оценка: 4

# Тернарный оператор (короткая запись if-else)
status = "отлично" if score > 80 else "нужно улучшить"
print(status)  # отлично
```

### 4. Циклы

>[!note]
>### **Теория:**
>Циклы повторяют блок кода. `for` используется для итерации по коллекциям, `while` выполняется пока условие истинно.

**Примеры:**
```python
# Цикл for по коллекциям
fruits = ["яблоко", "банан", "вишня"]
for fruit in fruits:
    print(f"Фрукт: {fruit}")

# for с range (генерация последовательности)
for i in range(5):           # 0, 1, 2, 3, 4
    print(f"Число: {i}")

# while с условием
counter = 0
while counter < 3:
    print(f"Счёт: {counter}")
    counter += 1  # Увеличиваем счётчик

# break и continue
for i in range(10):
    if i == 3:
        continue  # Пропускаем итерацию
    if i == 7:
        break     # Выходим из цикла
    print(i)      # 0, 1, 2, 4, 5, 6
```

### 5. Функции

>[!note]
>### **Теория:**
> Функции организуют код в переиспользуемые блоки. Могут принимать параметры и возвращать значения.

**Примеры:**
```python
# Простая функция
def greet(name):
    """Приветствует пользователя"""
    return f"Привет, {name}!"

print(greet("Анна"))  # Привет, Анна!

# Функция с параметрами по умолчанию
def introduce(name, age=18, city="Москва"):
    return f"{name}, {age} лет, из {city}"

print(introduce("Иван"))                 # Иван, 18 лет, из Москва
print(introduce("Мария", 25, "СПб"))     # Мария, 25 лет, из СПб

# Функция с произвольным числом аргументов
def sum_all(*numbers):
    """Суммирует все переданные числа"""
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3, 4, 5))  # 15

# Возврат нескольких значений
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([5, 2, 8, 1, 9])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9
```

### 6. Работа со строками

>[!note]
> ### **Теория:** 
> Строки в Python — неизменяемые последовательности символов с богатым набором методов.

**Примеры:**
```python
text = "Привет, мир!"

# Базовые методы
print(text.strip())           # "Привет, мир!" (убирает пробелы)
print(text.lower())           # "  привет, мир!  "
print(text.upper())           # "  ПРИВЕТ, МИР!  "
print(text.replace("мир", "Python"))  # "  Привет, Python!  "
print(text.split(","))        # ['  Привет', ' мир!  ']
print("мир" in text)          # True

# Форматирование строк
name = "Алексей"
age = 30

# f-строки (рекомендуется)
message1 = f"Имя: {name}, Возраст: {age}"
print(message1)

# format()
message2 = "Имя: {}, Возраст: {}".format(name, age)
print(message2)

# Срезы (slicing)
text = "Программирование"
print(text[0:6])      # Програ
print(text[7:])       # ммрование
print(text[-5:])      # ание (последние 5 символов)
print(text[::-1])     # еиневарморгорП (реверс)
```

### 7. Списки `(list)`

>[!note]
>### **Теория:**
> Списки — изменяемые упорядоченные коллекции. Поддерживают индексацию, срезы и множество методов.

**Примеры:**
```python
# Создание и базовые операции
numbers = [1, 2, 3, 4, 5]

numbers.append(6)        # [1, 2, 3, 4, 5, 6] - добавить в конец
numbers.insert(0, 0)     # [0, 1, 2, 3, 4, 5, 6] - вставить по индексу
numbers.remove(3)        # [0, 1, 2, 4, 5, 6] - удалить элемент
popped = numbers.pop()   # [0, 1, 2, 4, 5], popped = 6

# Срезы
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[2:5])      # [2, 3, 4]
print(numbers[:3])       # [0, 1, 2]
print(numbers[3:])       # [3, 4, 5]
print(numbers[::2])      # [0, 2, 4]
print(numbers[::-1])     # [5, 4, 3, 2, 1, 0]

# List comprehension (генератор списков)
squares = [x**2 for x in range(5)]          # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0] # [0, 2, 4, 6, 8]
pairs = [(x, y) for x in [1,2] for y in [3,4]]  # [(1,3), (1,4), (2,3), (2,4)]
```

### 8. Словари `(dict)`

>[!note]
> ### **Теория:**
> Словари — неупорядоченные коллекции пар ключ-значение. Ключи должны быть уникальными и неизменяемыми.

**Примеры:**
```python
# Создание словаря
person = {
    "name": "Иван",
    "age": 30,
    "city": "Москва",
    "skills": ["Python", "SQL", "Git"]
}

# Доступ к элементам
print(person["name"])                  # Иван
print(person.get("age"))               # 30
print(person.get("country", "Россия")) # Россия (значение по умолчанию)

# Изменение и добавление
person["age"] = 31                     # Обновить
person["email"] = "ivan@mail.ru"      # Добавить новую пару

# Удаление
email = person.pop("email")           # Удалить и вернуть значение
del person["city"]                    # Удалить ключ

# Итерация по словарю
for key in person:                    # По ключам
    print(key)

for value in person.values():         # По значениям
    print(value)

for key, value in person.items():     # По парам ключ-значение
    print(f"{key}: {value}")

# Dict comprehension
squares = {x: x**2 for x in range(5)}  # {0:0, 1:1, 2:4, 3:9, 4:16}
```

### 9. Множества `(set)` и кортежи `(tuple)`

>[!note]
> ### **Теория:** 
> Множества — неупорядоченные коллекции уникальных элементов. Кортежи — неизменяемые списки.

**Примеры:**
```python
# Множества
set1 = {1, 2, 3, 3, 4}      # {1, 2, 3, 4} (дубли удаляются)
set2 = {3, 4, 5, 6}

print(set1.union(set2))        # {1, 2, 3, 4, 5, 6} (объединение)
print(set1.intersection(set2)) # {3, 4} (пересечение)
print(set1.difference(set2))   # {1, 2} (разность)

# Кортежи
coordinates = (10.5, 20.3)
point = 30, 40  # Можно без скобок

# Распаковка кортежа
x, y = coordinates
print(f"X: {x}, Y: {y}")  # X: 10.5, Y: 20.3

# Кортеж как ключ словаря (т.к. неизменяем)
locations = {
    (55.7558, 37.6173): "Москва",
    (59.9343, 30.3351): "Санкт-Петербург"
}
```

### 10. Обработка исключений

>[!note]
> ### **Теория:**
>  Исключения позволяют корректно обрабатывать ошибки во время выполнения программы.

**Примеры:**
```python
# Базовый try/except
try:
    number = int(input("Введите число: "))
    result = 10 / number
    print(f"Результат: {result}")
except ValueError:
    print("Ошибка: нужно ввести число!")
except ZeroDivisionError:
    print("Ошибка: деление на ноль!")
except Exception as e:
    print(f"Неизвестная ошибка: {e}")
else:
    print("Вычисление прошло успешно!")
finally:
    print("Блок finally выполняется всегда.")

# Создание собственного исключения
class NegativeNumberError(Exception):
    """Исключение для отрицательных чисел"""
    pass

def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Число должно быть положительным")
    return number

try:
    check_positive(-5)
except NegativeNumberError as e:
    print(f"Ошибка: {e}")
```

### 11. Работа с файлами

>[!note]
> ### **Теория:**
> `Python` предоставляет простые способы чтения и записи файлов с автоматическим закрытием.

**Примеры:**
```python
# Запись в файл
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Первая строка\n")
    file.write("Вторая строка\n")
    file.write("Третья строка\n")

# Чтение файла целиком
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# Чтение построчно
with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())  # strip() убирает \n

# Добавление в файл
with open("data.txt", "a", encoding="utf-8") as file:
    file.write("Ещё одна строка\n")

# Чтение CSV-подобного файла
data = "Иван,30,Москва\nМария,25,СПб\n"
with open("people.csv", "w", encoding="utf-8") as file:
    file.write(data)

with open("people.csv", "r", encoding="utf-8") as file:
    for line in file:
        name, age, city = line.strip().split(",")
        print(f"{name} - {age} лет - {city}")
```

### 12. Модули и импорты
>[!note]
> ### **Теория:**
>  Модули позволяют организовывать код в отдельные файлы и повторно использовать его.

**Примеры:**
```python
# Импорт всего модуля
import math
print(math.sqrt(16))  # 4.0

# Импорт с псевдонимом
import datetime as dt
now = dt.datetime.now()

# Импорт конкретных функций
from random import randint, choice
print(randint(1, 10))          # Случайное число от 1 до 10
print(choice(["а", "б", "в"])) # Случайный элемент

# Создание собственного модуля
# В файле calculator.py:
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# В основном файле:
from calculator import add, multiply
print(add(5, 3))        # 8
print(multiply(5, 3))   # 15
```
### 13 Интерполяция строк

>[!note]
> ### **Теория:**
> Интерполяция — вставка значений переменных в строку. В `Python` есть несколько способов:

**Примеры:**

```python
name = "Иван"
age = 25
salary = 75000.50

# 1. f-строки (рекомендуется, Python 3.6+)
message = f"Меня зовут {name}, мне {age} лет"
print(message)  # Меня зовут Иван, мне 25 лет

# Выражения внутри f-строк
print(f"Через год мне будет {age + 1} лет")
print(f"Зарплата: {salary:,.2f} руб")  # 75,000.50 руб

# 2. format() метод (Python 2.6+, 3+)
message = "Меня зовут {}, мне {} лет".format(name, age)
print(message)

# С указанием позиций
message = "Меня зовут {0}, мне {1} лет. Повтор: {0}".format(name, age)

# С именованными параметрами
message = "Имя: {n}, возраст: {a}".format(n=name, a=age)

# 3. %-форматирование (старый стиль, как в C)
message = "Меня зовут %s, мне %d лет" % (name, age)
print(message)

# 4. Конкатенация (склеивание)
message = "Меня зовут " + name + ", мне " + str(age) + " лет"
print(message)
```
### 14. Возвратные функции
```py
a = 10

def is10():
    if a == 10:
        return True
    else:
        return False

if is10():
    print("a равно 10")
else:
    print("a не равно 10")
```
>[!note]
>### Теория:
>Если `a` = 10, то возвращается функция `True`, иначе - `False`
