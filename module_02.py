"""
Description: Module 02 demonstration
Author:Gaganpreet Kuar
Date:September 9, 2024
Usage: To demonstarte content from Module 02.


"""

# This is a single-line comment.

"""
This is a multi-line comment.

It can span multipe lines.

"""

absolute_value = abs(-12) # abs is absolute and ()Round brackets means A Function
print('Absolute value:', absolute_value) # '' means Text Literal


print('Absolute value:', abs(-12))

print("I am ", 25, "years old.")
print('I am ',25, 'years old.')
print("I am 20 years old.")
print(25)

print("Apples","Oranges","Banana")
print("Apples","Oranges","Banana", sep= ",")
print("Apples","Oranges","Banana", sep= "")

print("Print usinf f-string")
name = "John"
age = 25

print("My name is ",name,"and I am ",age,"years old.")

print(f"My name is {name} and I am {age} years old")
value = 3.149159
print(f"The value is {value}")

print(f"The value is {value:.2f}") # Rounding 

number = 123;
print(f"The number is {number:05}.") # Add Numbers

print(f"Hello, {name}")
print(f"Hello, {name:>10}") # Make this 10 characters long ...