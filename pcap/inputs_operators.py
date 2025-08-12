# Inputs and Operators

# Reading Input
# The input() function reads a line from input, returning it as a string.
name = input("Enter your name: ")  # Prompt user and read input as string
print("Hello,", name)  # Greet the user

# Type Casting
# Convert string input to integer
age_str = input("Enter your age: ")
age = int(age_str)  # Cast string to int
print("Your age is:", age)

# Convert string input to float
height_str = input("Enter your height in meters: ")
height = float(height_str)  # Cast string to float
print("Your height is:", height)

# Note: int() truncates floats towards zero
print(int(3.9))  # Outputs: 3
print(int(-3.9))  # Outputs: -3

# String Operators
# Concatenation with +
first = "Py"
second = "thon"
print(first + second)  # Outputs: Python

# Repetition with *
print("ha" * 3)  # Outputs: hahaha

# Mixing types requires explicit casting
age = 37
print("Age: " + str(age))  # Outputs: Age: 37

# Escaping and Special Characters
print("I\'m happy.")  # Single quote escaped
print("He said \"Python\".")  # Double quotes escaped
print("Line1\nLine2")  # Newline character
print("Column1\tColumn2")  # Tab character

# Pitfalls
# Uncommenting the following lines will cause errors

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# result = 5 + input("Enter a number: ")

# ZeroDivisionError: division by zero
# zero_div = 10 / 0

# ValueError: invalid literal for int() with base 10
# invalid_int = int("abc")

# Best Practices
# Always validate and cast user input before arithmetic operations
try:
    user_input = input("Enter a number to divide 100 by: ")
    num = float(user_input)
    result = 100 / num
    print("Result:", result)
except ValueError:
    print("That was not a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

# Summary
# input() returns strings; use int() or float() to convert for numeric operations.
# Use + and * for string concatenation and repetition.
# Escape quotes and special characters with backslash.
# Handle exceptions for invalid input and division errors to write robust code.