person = {
    "name": "Иван",
    "age": 30,
    "city": "Москва",
    "skills": ["Python", "SQL", "Git"]
}


print(person["name"])                 
print(person.get("age"))               
print(person.get("country", "Россия")) 

person["age"] = 31                     
person["email"] = "ivan@mail.ru"      


email = person.pop("email")           
del person["city"]                    


for key in person:                    
    print(key)

for value in person.values():         
    print(value)

for key, value in person.items():     
    print(f"{key}: {value}")


squares = {x: x**2 for x in range(5)}