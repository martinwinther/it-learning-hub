# The print() Function and Hello World
# This script demonstrates the simplest possible Python program
# and expands on the concepts from Section 2.1 of Python Essentials 1.

# In Python, programs are plain text files containing statements.
# Each statement tells the Python interpreter to perform an action.

# The print() function is one of Python's built-in functions.
# It sends text (or other data) to the standard output (usually the screen).
# Syntax: print(argument1, argument2, ...)
# Arguments are the values you want to display.

# Strings are sequences of characters enclosed in quotes.
# You can use either single quotes ('...') or double quotes ("...").
# They are functionally identical in Python.
# Example:
print("Hello, World")  # double quotes
print('Hello, World')  # single quotes

# Note: In Python 3, print is a function and requires parentheses.
# This will cause an error in Python 3:
# print "Hello, World"

# You can print multiple arguments, separated by commas.
print("Hello", "World", 2025)

# print() automatically adds a newline at the end.
# You can change this with the 'end' parameter:
print("Hello, ", end="")
print("World!")  # This will appear on the same line as the previous print.

# You can use n\ as a separator to print multiple lines
print("Hello", "\nWorld")

# The difference between file and interactive mode:
# - File mode: You save code in a .py file and run it with:
#       python3 hello_world.py
# - Interactive mode: You type code directly into the Python prompt (>>>),
#   and see the result immediately.

# Whitespace and indentation:
# Python ignores extra spaces between elements on the same line,
# but indentation at the beginning of a line is syntactically significant
# and is used to define blocks of code (functions, loops, conditionals, etc.).

# Example with intentional spacing (valid):
print(   "Spacing is ignored inside parentheses"   )

# Example of an invalid indentation (will cause an IndentationError if uncommented):
#     print("This line starts with unnecessary indentation")

# Summary:
# - Python code is made of statements.
# - print() outputs data to the screen.
# - Strings can be enclosed in single or double quotes.
# - In Python 3, parentheses are mandatory for print().
# - Whitespace inside a line is mostly ignored; indentation matters.