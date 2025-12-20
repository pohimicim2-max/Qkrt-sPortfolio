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


class NegativeNumberError(Exception):
    pass

def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Число должно быть положительным")
    return number

try:
    check_positive(-5)
except NegativeNumberError as NegativeError:
    print(f"Ошибка: {NegativeError}")