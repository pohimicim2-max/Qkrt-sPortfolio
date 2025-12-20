local Players = game:GetService("Players")
local Workspace = game:GetService("Workspace")


local part = Instance.new("Part")
part.Name = "MyPart"
part.Size = Vector3.new(5, 5, 5)
part.Position = Vector3.new(0, 10, 0)
part.Parent = Workspace


local function onPlayerAdded(player)
    print(player.Name .. " присоединился!")
    
    
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