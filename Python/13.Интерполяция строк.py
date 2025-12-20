name = "Иван"
age = 25
salary = 75000.50


message = f"Меня зовут {name}, мне {age} лет"
print(message)


print(f"Через год мне будет {age + 1} лет")
print(f"Зарплата: {salary:,.2f} руб")


message = "Меня зовут {}, мне {} лет".format(name, age)
print(message)


message = "Меня зовут {0}, мне {1} лет. Повтор: {0}".format(name, age)


message = "Имя: {n}, возраст: {a}".format(n=name, a=age)


message = "Меня зовут %s, мне %d лет" % (name, age)
print(message)


message = "Меня зовут " + name + ", мне " + str(age) + " лет"
print(message)