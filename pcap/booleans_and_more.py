# Boolean values and expressions in Python

# Boolean type: True and False
# In Python, the Boolean type has only two values: True and False.
# They are case-sensitive and always start with a capital letter.

a = True
b = False

print("a:", a)  # True
print("b:", b)  # False

# Numeric equivalents:
# True is equivalent to 1, False is equivalent to 0
print("True + 1 =", True + 1)   # 2
print("False + 1 =", False + 1) # 1

# Comparison operators:
# Used to compare values and produce a Boolean result.
x = 10
y = 20

print("x == y:", x == y)   # False, equal to
print("x != y:", x != y)   # True, not equal to
print("x < y:", x < y)     # True, less than
print("x <= y:", x <= y)   # True, less than or equal to
print("x > y:", x > y)     # False, greater than
print("x >= y:", x >= y)   # False, greater than or equal to

# Boolean operators:
# and, or, not - used to combine or invert Boolean values.

# Truth tables for and, or, not
# and: True if both operands are True
print("True and True:", True and True)     # True
print("True and False:", True and False)   # False
print("False and True:", False and True)   # False
print("False and False:", False and False) # False

# or: True if at least one operand is True
print("True or True:", True or True)       # True
print("True or False:", True or False)     # True
print("False or True:", False or True)     # True
print("False or False:", False or False)   # False

# not: inverts the Boolean value
print("not True:", not True)   # False
print("not False:", not False) # True

# Combining comparisons with logical operators
age = 25
has_license = True

# Check if person is an adult AND has a license
can_drive = (age >= 18) and has_license
print("Can drive:", can_drive)  # True

# Check if person is a minor OR does not have a license
cannot_drive = (age < 18) or (not has_license)
print("Cannot drive:", cannot_drive) # False

# Using bool() to convert other types to Boolean
print("bool(0):", bool(0))           # False
print("bool(1):", bool(1))           # True
print("bool(\"\"):", bool(""))       # False
print("bool(\"hello\"):", bool("hello")) # True
print("bool(None):", bool(None))     # False
print("bool([]):", bool([]))         # False
print("bool([1, 2, 3]):", bool([1, 2, 3])) # True

# Common pitfalls:

# Assignment (=) vs comparison (==)
x = 5
# if x = 5:    # This will cause a SyntaxError!
#     print("x is 5")

# Correct way:
if x == 5:
    print("x is 5")

# Chaining comparisons
num = 15
# Python allows chaining comparisons like this:
print("10 < num < 20:", 10 < num < 20)  # True

# Equivalent to:
print("(10 < num) and (num < 20):", (10 < num) and (num < 20))  # True

# Summary:
# - Boolean values are True or False.
# - Comparison operators return Boolean results.
# - Logical operators (and, or, not) combine or invert Booleans.
# - bool() converts values to Boolean: zero, empty, None are False; others True.
# - Use == for comparison, not =.
# - Comparisons can be chained for readability.
