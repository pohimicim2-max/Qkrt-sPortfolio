function addNumbers(a, b)
    return a + b
end

local multiply = function(a, b)
    return a * b
end


local health = 75
if health > 50 then
    print("Здоровье в порядке")
elseif health > 25 then
    print("Мало здоровья")
else
    print("Критическое состояние!")
end

for i = 1, 10 do
    print("Итерация " .. i)
end

local count = 0
while count < 5 do
    print(count)
    count = count + 1
end