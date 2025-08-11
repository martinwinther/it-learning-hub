# Variables, Comments, Input & Casting, and String Operators
# ---------------------------------------------------------
# This script collects the remaining beginner building blocks:
# - Variables and assignment (creating, naming, reassigning)
# - Comments (how and why to use them)
# - Reading input from the user with input()
# - Converting strings to numbers and back (type casting)
# - Basic string operators: + (concatenation) and * (repetition)
#
# All examples are safe to run. Lines that would error are left commented with explanations.

print("=== VARIABLES ===")

# Creating and assigning variables (Python creates a variable on first assignment)
distance_km = 150       # integer
time_hours = 2.5        # float
vehicle = "car"         # string
is_raining = False      # boolean

# Reading and using variable values
avg_speed = distance_km / time_hours  # expression using variables
print("Average speed (km/h):", avg_speed)

# Reassigning variables (names are labels; values can change)
distance_km = 300
time_hours = 4
avg_speed = distance_km / time_hours
print("Updated average speed (km/h):", avg_speed)

# Multiple assignment
x, y, z = 1, 2, 3
print("x, y, z ->", x, y, z)

# Swapping values (Pythonic)
a, b = 10, 20
a, b = b, a
print("Swapped a, b ->", a, b)

# Augmented assignment (shortcut operators)
counter = 0
counter += 1   # same as: counter = counter + 1
counter *= 5   # same as: counter = counter * 5
counter -= 2
counter //= 3  # integer division
print("Counter:", counter)

# Valid variable names: letters, digits (not as first char), underscores.
snake_case_is_recommended = True
_underscore_prefix = "often used for 'private' or internal"
name2 = "ok"
# Invalid examples (leave commented)
# 2name = "nope"
# first-name = "nope"
# class = "nope"  # 'class' is a keyword

# Naming tips:
# - Use lowercase_with_underscores.
# - Avoid shadowing built-ins: e.g., don't name a variable 'list', 'dict', 'str', 'sum', 'input', etc.

print("\n=== COMMENTS ===")

# Single-line comments start with '#'.
# Use them to explain *why* or *intent*, not the obvious *what*.

speed_limit = 110  # km/h on motorways in some countries

# "Block comments": just multiple single-line comments.
# You may also use a multi-line string as a docstring at module/function/class level,
# but remember: triple-quoted strings are *strings*, not comments. They are executed at runtime
# and become the __doc__ attribute when placed immediately after a definition.

def kmh_to_ms(kmh):
    """Convert kilometers per hour to meters per second (1 km/h ≈ 0.27778 m/s)."""
    return kmh * (1000/3600)

print("120 km/h in m/s:", kmh_to_ms(120))

# Commenting out code to "disable" a fragment:
# print("This won't run")

print("\n=== INPUT & CASTING ===")

# input() reads a line from standard input and returns a *string*.
# Example (interactive). Uncomment to try.
# name = input("Your name: ")
# print("Hello,", name)

# Converting strings to numbers (type casting):
# - int(text) -> integer (text must represent an integer in base 10 by default)
# - float(text) -> floating-point number (allows decimals and scientific notation)
sample_int = int("42")
sample_float = float("3.14")
sci = float("1e3")  # 1000.0
print("Casts:", sample_int, sample_float, sci)

# Casting pitfalls (leave commented to avoid runtime errors):
# int("3.14")      # ValueError (string is not a valid integer)
# int("forty two") # ValueError
# float("NaN")     # Works in Python: returns float('nan'), but may surprise beginners

# Casting numbers to strings for concatenation/display
answer = 42
print("The answer is " + str(answer))   # must cast non-strings before concatenating with +

# Casting floats to int truncates toward zero
print("int(3.99) ->", int(3.99))
print("int(-3.99) ->", int(-3.99))

# Read numbers from the user safely (example function; call when you want interaction)
def read_two_numbers():
    """Prompt for two numbers and return them as floats. Handles bad input."""
    while True:
        try:
            a_text = input("Enter first number: ")
            b_text = input("Enter second number: ")
            a = float(a_text)
            b = float(b_text)
            return a, b
        except ValueError:
            print("Please enter numeric values, e.g., 3 or 3.14.")

# Example usage (interactive). Uncomment to try.
# a, b = read_two_numbers()
# print("Sum:", a + b)

print("\n=== STRING OPERATORS (+, *) ===")

# Concatenation (+) joins strings
hello = "Hello"
world = "World"
print(hello + " " + world + "!")

# Repetition (*) repeats a string n times
print("ha" * 3)  # 'hahaha'

# Mixed types with + cause TypeError unless you cast
age = 37
print("Age: " + str(age))

# Newlines and escaping
print("First line\nSecond line")
print('I\'m learning Python.')
print("He said \"Python\".")

# Strings are sequences: length and simple indexing
s = "Python"
print("Length:", len(s), "First char:", s[0], "Last char:", s[-1])

# Immutability reminder: strings can't be modified in place; create new strings instead.
t = s.replace("Py", "Ry")
print("Original:", s, "| New:", t)

print("\n=== INPUT: PROMPTS & PROHIBITED OPERATIONS ===")

# input() can take a prompt string
# n_text = input("Enter an integer: ")
# print("You typed:", n_text)

# Prohibited/unsafe operations examples (left commented so the file runs clean):
# - Using + between string and number without casting:
# print("Result: " + 5)        # TypeError
# - Dividing by zero:
# print(1 / 0)                 # ZeroDivisionError
# - Converting non-numeric text to int/float:
# int("twelve")                # ValueError

print("\nAll examples completed.")