num1 = float(input("Enter the first number: "))
operator = input("Enter an operaror (+,-,*,/,%): ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(f"Your sum is: {round(result, 2)}")
elif operator == "-":
    result = num1 - num2
    print(f"Your sub is: {round(result, 2)}")
elif operator == "*":
    result = num1 * num2
    print(f"Your mult is: {round(result, 2)}")
elif operator == "/":
    result = num1 / num2
    print(f"Your div is: {round(result, 2)}")
elif operator == "%":
    result = num1 % num2
    print(f"Your mod is: {round(result, 2)}")
else:
    print("Invalid Operator!")