# ---------------- Python Basics - 1 ---------------- #
# Variables in Python
# Variables store data values. No need to declare type (Python is dynamically typed).

# ---------------- Syntax for Variable Assignment ---------------- #
x = 5       # Assigning an integer value
y = "Hello" # Assigning a string value

# ---------------- Variable Naming Rules ---------------- #
# - Can contain letters (a-z, A-Z), numbers (0-9), and underscores (_)
# - Must start with a letter or underscore
# - Case-sensitive (Name != name)

# Example:
age = 25
name = "John"
is_student = True

print("Variables Example:")
print(age)
print(name)
print(is_student)

# ---------------- Data Types in Python ---------------- #
# int → integers
# float → floating-point numbers
# str → strings
# bool → boolean values

x = 10
print("\nData Type Example:")
print(x, type(x))  # Output: 10 <class 'int'>

# ---------------- Type Conversion ---------------- #
x = "10"       # string
y = int(x)     # convert string to integer
z = float(y)   # convert integer to float
print("\nType Conversion Example:")
print(z)       # Output: 10.0

# ---------------- Arithmetic Operators ---------------- #
a = 10
b = 3

print("\nArithmetic Operators Example:")
print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.3333...
print("Floor Division:", a // b) # 3
print("Modulus:", a % b)         # 1
print("Exponentiation:", a ** b) # 1000

# ---------------- Assigning Values to Multiple Variables ---------------- #
x, y, z = 10, 20, 30
print("\nMultiple Variable Assignment Example:")
print(x, y, z)  # 10 20 30

x = y = z = 100
print(x, y, z)  # 100 100 100

# ---------------- Variable Reassignment ---------------- #
x = 5
print("\nVariable Reassignment Example:")
print(x)  # 5
x = 10
print(x)  # 10
