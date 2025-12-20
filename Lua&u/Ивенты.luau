local part = script.Parent

part.Touched:Connect(function(otherPart)
    local humanoid = otherPart.Parent:FindFirstChild("Humanoid")
    if humanoid then
        humanoid.Health = humanoid.Health - 10
        print("Игрок получил урон!")
    end
end)


local function countdown()
    for i = 3, 1, -1 do
        print(i)
        task.wait(1)
    end
    print("Старт!")
end

coroutine.wrap(countdown)()