def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "cannot be divisible by 0"
        return num1 / num2
    elif operator == "%":
        return num1 % num2
    else:
        return "invalid operator"
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operator = input("Choose your operator:\nAddition(+)\nSubtraction(-)\nMultiplication(*)\nDivision(/)\nModulus(%)\n")

print(calculator(num1, num2, operator))