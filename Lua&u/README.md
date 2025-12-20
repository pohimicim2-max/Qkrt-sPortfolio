<div align="center">

# Lua/u
### Всё, что связано с Луа/у (`Lua/u`)
</div>

>[!note]
> ### Определение
> **Luau (произносится "луау")** — это высокоуровневый, быстрый, постепенно типизированный язык программирования, созданный Roblox на основе Lua 5.1. Это основной язык скриптинга в Roblox Studio для создания игр и интерактивного контента.

>[!note]
> ### Lua
> в Роблокс студио был `Lua`, который позже устарел и был заменён `Luau`

>[!tip]
> ### Оффициальная документация
> Офф. документация роблокса по этой ссылке:
> ### **https://create.roblox.com/docs**

# Время к **Базовому синтаксу**
Комментарий
```lua
-- комментарий
```
Вывод в терминал
```lua
print("Hello, World!")
```
Вывод ошибок и предупреждений
```lua
warn("Ошибка")
error("Скрипт больше не работает")
```
>[!caution]
>### error
> Обратите внимание, что после `error()` **ничего** не обрабатывается.
### Пример:
```lua
error("Ошибка")
print("привет") -- НЕ БУДЕТ ОБРАБАТЫВАТЬСЯ. Роблокс будет предупреждать всегда
```
Переменные
```lua
local player = "Player1"
local health = 100
local bool = true
local v1 = 10
local v2 = 20
```
>[!warning]
> ### Переменные
> В `lua` переменные можно писать и без `local`, но из-за этого они станут глобальными и менее работоспособными.
> ### Bool
> Также обратите внимание, что тип данных, как `bool` пишется с **строчной** буквы (вместо питона)

Типы данных
```lua
local str = "string"
local num = 100 -- (любое интовое число)
local bool = true or false
local NilValue = nil
local table = {1, 2, 3}
```

### Обычный скрипт на примере:
```lua
-- Получение сервиса
local Players = game:GetService("Players")
local Workspace = game:GetService("Workspace")

-- Создание части
local part = Instance.new("Part")
part.Name = "MyPart"
part.Size = Vector3.new(5, 5, 5)
part.Position = Vector3.new(0, 10, 0)
part.Parent = Workspace

-- Обработка игроков
local function onPlayerAdded(player)
    print(player.Name .. " присоединился!")
    
    -- Создание character
    player.CharacterAdded:Connect(function(character)
        local humanoid = character:FindFirstChild("Humanoid")
        if humanoid then
            humanoid.Died:Connect(function()
                print(player.Name .. " умер")
            end)
        end
    end)
end

Players.PlayerAdded:Connect(onPlayerAdded)
```

### Функции и управление потоком
```lua
-- Функции
function addNumbers(a, b)
    return a + b
end

local multiply = function(a, b)
    return a * b
end

-- Условия
local health = 75
if health > 50 then
    print("Здоровье в порядке")
elseif health > 25 then
    print("Мало здоровья")
else
    print("Критическое состояние!")
end

-- Циклы
for i = 1, 10 do
    print("Итерация " .. i)
end

local count = 0
while count < 5 do
    print(count)
    count = count + 1
end
```
### Таблицы
```lua
-- Массив
local fruits = {"apple", "banana", "orange"}
print(fruits[1])  -- "apple" (индексация с 1!)

-- Словарь
local player = {
    Name = "Alex",
    Score = 100,
    Level = 5
}
print(player.Name)  -- "Alex"

-- Итерация
for index, fruit in ipairs(fruits) do
    print(index, fruit)
end

for key, value in pairs(player) do
    print(key, value)
end
```
>[!warning]
>### Индекс списка
> Индексация списка начинается **всегда** с единицы (1).

### Ивенты
```lua
-- События (важная концепция роблокса)
local part = script.Parent

part.Touched:Connect(function(otherPart)
    local humanoid = otherPart.Parent:FindFirstChild("Humanoid")
    if humanoid then
        humanoid.Health = humanoid.Health - 10
        print("Игрок получил урон!")
    end
end)

-- Coroutines (асинхронность)
local function countdown()
    for i = 3, 1, -1 do
        print(i)
        task.wait(1)  -- Аналог wait(), но лучше
    end
    print("Старт!")
end

coroutine.wrap(countdown)()  -- Запуск корутины
```

>[!tip]
>### Для начало работы в роблокс студио:
>1. Создайте новый скрипт (`Script` для сервера, `LocalScript` для клиента)
>2. Поместите в объект (`Part`, `Model`, `Player`)
>3. Используйте встроенный редактор с подсветкой синтаксиса
>4. Тестировать можно через кнопку **Play**

>[!note]
> ### Модульные скрипты (`ModuleScript`)
> **Модульные скрипты** **(`ModuleScript`)** - это **скрипты-библиотеки** или **готовые куски кода**

