# Python Basics

# -------------------------------
# 1. Variables and Data Types
# -------------------------------
# Python automatically detects type

name = "Alice"  # string
age = 20        # integer
height = 5.7    # float
is_student = True  # boolean

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# -------------------------------
# 2. Comments
# -------------------------------
# This is a single-line comment

"""
This is a multi-line comment
It can span multiple lines
"""

# -------------------------------
# 3. Operators
# -------------------------------
a = 10
b = 3

# Arithmetic
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# Comparison
print("a > b:", a > b)
print("a == b:", a == b)

# Logical
print("a > 5 and b < 5:", a > 5 and b < 5)
print("a > 5 or b > 5:", a > 5 or b > 5)
print("not(a > b):", not(a > b))

# -------------------------------
# 4. Lists
# -------------------------------
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)
print("First fruit:", fruits[0])

fruits.append("orange")  # add
fruits.remove("banana")  # remove
print("Updated Fruits:", fruits)

# -------------------------------
# 5. Loops
# -------------------------------
# For loop
for fruit in fruits:
    print("Fruit:", fruit)

# While loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1

# -------------------------------
# 6. Conditional Statements
# -------------------------------
number = 15

if number > 20:
    print("Number is greater than 20")
elif number > 10:
    print("Number is greater than 10 but less than or equal to 20")
else:
    print("Number is 10 or less")

# -------------------------------
# 7. Functions
# -------------------------------
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# -------------------------------
# 8. Dictionaries
# -------------------------------
student = {
    "name": "Alice",
    "age": 20,
    "grades": [85, 90, 78]
}

print("Student Name:", student["name"])
print("Student Grades:", student["grades"])

# -------------------------------
# 9. Input from User
# -------------------------------
# Uncomment to test input
# user_name = input("Enter your name: ")
# print("Hello", user_name)

# -------------------------------
# 10. Importing Modules
# -------------------------------
import math
print("Square root of 16:", math.sqrt(16))

# -------------------------------
# 11. File Handling
# -------------------------------
# Write to a file
with open("example.txt", "w") as f:
    f.write("Hello Python!\n")

# Read from a file
with open("example.txt", "r") as f:
    content = f.read()
    print("File Content:", content)
