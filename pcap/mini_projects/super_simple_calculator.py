"""
This program is a simple calculator that asks the user to enter two numbers and an arithmetic operator (+, -, *, /).
It calculates all four operations (addition, subtraction, multiplication, and division) but only keeps the one matching the chosen operator.
This works because in Python, True is treated as 1 and False is treated as 0, so only the selected operation contributes to the result.
Example: if the operator is '+', it becomes: (1 * (a + b)) + (0 * (a - b)) + (0 * (a * b)) + (0 * (a / b)) →  sum + 0 + 0 + 0
Example: if a = 5, b = 3, and the operator is '+', it becomes: (1 * (5 + 3)) + (0 * (5 - 3)) + (0 * (5 * 3)) + (0 * (5 / 3)) →  8 + 0 + 0 + 0
"""

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operator = input("Enter an action (+, -, *, /): ")

try:
    result = (operator == "+") * (a + b) + (operator == "-") * (a - b) + (operator == "*") * (a * b) + (operator == "/") * (a / b)
    print(a, operator, b, "=", result)
except ZeroDivisionError:
    print("Division by zero is not allowed.")