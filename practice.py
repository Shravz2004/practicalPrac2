# Simple Calculator in Python

# Take input from user
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -): ")
num2 = float(input("Enter second number: "))

# Perform operation
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operator"


# Output the result
print("Result:", result)
