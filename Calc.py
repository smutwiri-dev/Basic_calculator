# Basic Calculator Program
# This program can add, subtract, multiply, and divide two numbers.

# Ask the user to input the first number
# float() for decimal compatibility.
num1 = float(input("Enter the first number: "))

# Ask the user to input the second number
# float() for decimal compatibility
num2 = float(input("Enter the second number: "))

# Addition of the two numbers
sum_result = num1 + num2

# Subtraction: first number minus the second
difference_result = num1 - num2

# Multiplication of the two numbers
product_result = num1 * num2

# Divide the first number by the second 
quotient_result = num1 / num2

# Calculation results
print(f"Calculation Results:")
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}") 
print(f"Product: {product_result}")
print(f"Quotient: {quotient_result}")