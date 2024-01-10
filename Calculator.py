num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
operator = input("Enter an Operator(+-/*):")

if operator == "+":
    total = num1 + num2 
elif operator == "-":
    total = num1 - num2
elif operator == "/":
    total = num1 / num2 
elif operator == "*":
    total = num1 * num2
else:
    print("Invalid operator")

print(total)