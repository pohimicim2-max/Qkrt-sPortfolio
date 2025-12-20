def greet(name):  
    return f"Привет, {name}!"

print(greet("Анна"))

def introduce(name, age=18, city="Москва"):
    return f"{name}, {age} лет, из {city}"

print(introduce("Иван"))                 
print(introduce("Мария", 25, "СПб"))     

def sum_all(*numbers):
    """Суммирует все переданные числа"""
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3, 4, 5))

def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([5, 2, 8, 1, 9])
print(f"Min: {minimum}, Max: {maximum}")  