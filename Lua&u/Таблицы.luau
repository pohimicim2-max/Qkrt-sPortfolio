local fruits = {"apple", "banana", "orange"}
print(fruits[1])

local player = {
    Name = "Alex",
    Score = 100,
    Level = 5
}
print(player.Name)

for index, fruit in ipairs(fruits) do
    print(index, fruit)
end

for key, value in pairs(player) do
    print(key, value)
end