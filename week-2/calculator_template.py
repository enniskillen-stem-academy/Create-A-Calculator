# Calculator Challenge: Create a basic calculator
# Instructions: Complete the code to perform basic arithmetic operations.

# 1. Ask the user for two numbers.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# 2. Ask the user to choose an operation: +, -, *, /
operation = input("Choose an operation (+, -, *, /): ")

# 3. Perform the chosen operation and print the result.
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "Invalid operation"

print("Result:", result)

# Experiment: Add error handling for division by zero or invalid input.
