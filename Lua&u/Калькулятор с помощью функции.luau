function calculator(a, b, op)
    if op == "*" then
        return a * b
        elseif op == "/" then
            return a / b
            elseif op == "+" then
                return a + b
                elseif op == "-" then
                    return a - b
                    else
                        return false
                        end

    end
calculator(5, 3, "*")
