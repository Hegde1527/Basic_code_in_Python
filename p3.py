# ---------------- Python Basics - 2 ---------------- #
# Input/Output, String Manipulation, Comments, and Escape Sequences

# ---------------- 1. Input and Output ---------------- #
# Input from the user using input()
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Convert input to integer

# Output using + operator
print("Hello, " + name + "! You are " + str(age) + " years old.")

# Output using f-string
print(f"Hello, {name}! You are {age} years old.")

# ---------------- 2. String Manipulation ---------------- #

# 2.1 Concatenation and Repetition
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("\nFull Name:", full_name)  # John Doe

greeting = "Hello! " * 3
print("Repeated Greeting:", greeting)  # Hello! Hello! Hello! 

# 2.2 String Methods
message = "  Hello, World!  "
print("Stripped:", message.strip())               # Remove spaces
print("Uppercase:", message.upper())             # Uppercase
print("Lowercase:", message.lower())             # Lowercase
print("Replaced:", message.replace("World", "Python"))  # Replace substring

# 2.3 Accessing String Characters (Indexing)
text = "Python"
print("\nFirst character:", text[0])  # P
print("Third character:", text[2])    # t
print("Last character:", text[-1])    # n
print("Third last character:", text[-3])  # h

# 2.4 Slicing Strings
text2 = "Python Programming"
print("Slice 0-5:", text2[0:6])  # Python
print("Slice start-5:", text2[:6])  # Python
print("Slice 7-end:", text2[7:])  # Programming

# ---------------- 3. Comments ---------------- #
# Single-line comment
print("\nHello, World!")  # Prints message

"""
Multi-line comment
This can span multiple lines
and is ignored by Python interpreter.
"""
print("Hello, Python!")

# ---------------- 4. Escape Sequences ---------------- #
print("\nEscape Sequences Examples:")
print("New line example:\nHello\nWorld")
print("Tab example:\tHello Python")
print("Backslash example: This is a backslash \\")

# ---------------- Optional Exercises ---------------- #
# 1. Character counter (excluding spaces)
user_string = input("\nEnter a string for character count: ")
count = len(user_string.replace(" ", ""))  # Remove spaces before counting
print("Number of characters (excluding spaces):", count)
