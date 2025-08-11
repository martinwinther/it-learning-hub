# Literals, Operators, and Expressions
# This script demonstrates the core building blocks of Python programs:
# values (literals), the symbols that act on them (operators), and how they combine into expressions.

# --- Literals ---
# A literal is a fixed value directly written into the code.

# String literals (text values enclosed in quotes)
print("This is a string literal")
print('Strings can use single quotes too')

# Escaping quotes (use backslash) and alternating quote types
print('I\'m happy.')                     # escape apostrophe inside single-quoted string
print("I'm happy.")                      # or use double quotes to avoid escaping
print('He said "Python", not "typhoon"') # double quotes inside single quotes
print("He said \"Python\", not \"typhoon\"")  # escaped double quotes inside double quotes

# Numeric literals
print(42)         # integer literal
print(3.14)       # floating-point literal

# Integer literals in other bases (binary, octal, hexadecimal)
print(0b1010)   # binary literal (base 2) -> 10 in decimal
print(0o12)     # octal literal  (base 8) -> 10 in decimal
print(0xA)      # hex literal    (base 16) -> 10 in decimal

# Converting to see decimal values explicitly
print(int(0b1010), int(0o12), int(0xA))  # 10 10 10

# Boolean literals
print(True)
print(False)

# Booleans in numeric contexts (True == 1, False == 0)
print(int(True), int(False))   # 1 0
print(True + True + 3)         # 5
print(False * 10)              # 0

# Special literal
print(None)       # represents 'no value' or 'null'

# --- Operators ---
# Operators are special symbols or keywords that perform operations on values.

# Arithmetic operators
# Unary operators (operate on a single operand)
print(-5)   # unary minus, changes the sign
print(+3)   # unary plus, usually leaves the value unchanged

# Binary operators (operate on two operands)
print(4 + 5)   # addition
print(12 % 5)  # modulus

print(5 + 3)   # addition
print(5 - 3)   # subtraction
print(5 * 3)   # multiplication
print(5 / 3)   # division (returns a float)
print(5 // 3)  # floor division (integer result)
print(5 % 3)   # modulo (remainder)
print(2 ** 3)  # exponentiation

# Comparison operators (return True or False)
print(5 == 3)   # equal to
print(5 != 3)   # not equal to
print(5 > 3)    # greater than
print(5 < 3)    # less than
print(5 >= 3)   # greater than or equal to
print(5 <= 3)   # less than or equal to

# Logical operators
print(True and False)  # logical AND
print(True or False)   # logical OR
print(not True)        # logical NOT

# --- Expressions ---
# An expression is a combination of literals, variables, operators, and function calls that produces a value.

result = (5 + 3) * 2
print(result)  # (5 + 3) happens first, then multiplied by 2

# Expressions can be just a single literal
print(100)

# Or involve multiple operations
print(10 - 4 / 2)  # division happens before subtraction

# --- Operator Precedence ---
# Python follows a specific hierarchy of priorities:
# 1. Parentheses ()
# 2. Exponentiation ** (right-sided binding)
# 3. Unary + and - (when applied to a single operand)
# 4. Multiplication, Division, Floor Division, Modulo (*, /, //, %)
# 5. Addition and Subtraction (+, -)
# 6. Comparisons (==, !=, <, >, <=, >=)
# 7. Logical NOT
# 8. Logical AND
# 9. Logical OR

print(2 + 3 * 4)      # Multiplication happens before addition → 14
print((2 + 3) * 4)    # Parentheses change the order → 20
# Right-sided binding of exponentiation
print(2 ** 2 ** 3)  # interpreted as 2 ** (2 ** 3) -> 2 ** 8 -> 256

# --- Common Mistakes ---
# Mixing types without understanding conversions
print("The answer is " + str(42))  # Must convert number to string for concatenation
# print("The answer is " + 42)     # This would cause a TypeError

# Integer division vs float division
print(5 / 2)   # 2.5 (float)
print(5 // 2)  # 2   (integer)

# --- Summary ---
# - Literals: fixed values in code (strings, numbers, booleans, None)
# - Operators: symbols that act on values (arithmetic, comparison, logical)
# - Expressions: combinations of literals and operators that produce a value
# - Precedence: determines the order in which operations are performed