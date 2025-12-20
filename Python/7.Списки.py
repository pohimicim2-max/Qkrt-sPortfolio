numbers = [1, 2, 3, 4, 5]

numbers.append(6)       
numbers.insert(0, 0)     
numbers.remove(3)        
popped = numbers.pop()   


numbers = [0, 1, 2, 3, 4, 5]
print(numbers[2:5])      
print(numbers[:3])       
print(numbers[3:])       
print(numbers[::2])      
print(numbers[::-1])     


squares = [x**2 for x in range(5)]          
evens = [x for x in range(10) if x % 2 == 0]
pairs = [(x, y) for x in [1,2] for y in [3,4]] 