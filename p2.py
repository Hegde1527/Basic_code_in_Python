# ---------------- Variables and Data Types in Python ---------------- #

# 1. Variables
# Variables store data values. No need to declare type (Python is dynamically typed).

a = 10
b = 20

print(a)       # prints value of a
print(b)       # prints value of b
print("a")     # prints the string "a"
print(a + b)   # prints sum of a and b

# Variable Naming Rules:
# - Can contain letters, numbers, and underscores
# - Must start with a letter or underscore
# - Case-sensitive (Name != name)

name = "John"
age = 25
is_student = True

# 2. Data Types
# int    -> integer numbers
# float  -> decimal numbers
# str    -> string
# bool   -> True or False

x = 10
print(type(x))  # <class 'int'>

# 3. Type Conversion
x = "10"      # string
y = int(x)    # convert to integer
z = float(y)  # convert to float
print(z)      # 10.0

# 4. Arithmetic Operators
a = 10
b = 3

print(a + b)  # addition
print(a - b)  # subtraction
print(a * b)  # multiplication
print(a / b)  # division
print(a // b) # floor division
print(a % b)  # modulus
print(a ** b) # exponentiation

# 5. Multiple Variable Assignment
x, y, z = 10, 20, 30
print(x, y, z)  # 10 20 30

x = y = z = 100
print(x, y, z)  # 100 100 100

# 6. Variable Reassignment
x = 5
print(x)  # 5
x = 10
print(x)  # 10
