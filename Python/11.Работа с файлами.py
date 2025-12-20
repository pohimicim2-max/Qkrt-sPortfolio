with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Первая строка\n")
    file.write("Вторая строка\n")
    file.write("Третья строка\n")


with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())


with open("data.txt", "a", encoding="utf-8") as file:
    file.write("Ещё одна строка\n")


data = "Иван,30,Москва\nМария,25,СПб\n"
with open("people.csv", "w", encoding="utf-8") as file:
    file.write(data)

with open("people.csv", "r", encoding="utf-8") as file:
    for line in file:
        name, age, city = line.strip().split(",")
        print(f"{name} - {age} лет - {city}")