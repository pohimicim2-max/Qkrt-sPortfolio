a = 10

function Test()
if a ~= 10 then
return false 
    end
end

if Test() then
    print(a == a)
else
    print(a ~= a)
end