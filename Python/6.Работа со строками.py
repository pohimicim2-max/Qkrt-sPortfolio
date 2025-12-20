text = "Привет, мир!"


print(text.strip())           
print(text.lower())          
print(text.upper())           
print(text.replace("мир", "Python"))  
print(text.split(","))       
print("мир" in text)          


name = "Алексей"
age = 30


message1 = f"Имя: {name}, Возраст: {age}"
print(message1)


message2 = "Имя: {}, Возраст: {}".format(name, age)
print(message2)


text = "Программирование"
print(text[0:6])      
print(text[7:])       
print(text[-5:])      
print(text[::-1])     