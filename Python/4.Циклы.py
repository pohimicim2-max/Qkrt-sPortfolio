fruits = ["яблоко", "банан", "вишня"]
for fruit in fruits:
    print(f"Фрукт: {fruit}")


for i in range(5):           
    print(f"Число: {i}")


counter = 0
while counter < 3:
    print(f"Счёт: {counter}")
    counter += 1  


for i in range(10):
    if i == 3:
        continue  
    if i == 7:
        break     
    print(i)      