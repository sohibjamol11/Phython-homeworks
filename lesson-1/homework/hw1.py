Homework:

Given a side of square. Find its perimeter and area.
Given diameter of circle. Find its length.
Given two numbers a and b. Find their mean.
Given two numbers a and b. Find their sum, product and square of each number.
----------------------
  # Input: side of the square
side = float(input("Enter the side length of the square: "))
# Calculate perimeter and area
perimeter = 4 * side
area = side ** 2
# Output the results
print(f"Perimeter of the square: {perimeter}")
print(f"Area of the square: {area}")
----------------------
import math

# Input: diameter of the circle
diameter = float(input("Enter the diameter of the circle: "))

# Calculate the length (circumference)
length = math.pi * diameter

# Output the result
print("The length (circumference) of the circle is:", round(length, 2))
-----------------------
# Input two numbers
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))

# Calculate the mean
mean = (a + b) / 2

# Output the result
print("The mean of", a, "and", b, "is:", mean)
-----------------------
# Input two numbers
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))

# Calculate sum, product, and squares
sum_ab = a + b
product_ab = a * b
square_a = a ** 2
square_b = b ** 2

# Display results
print("\nResults:")
print("Sum =", sum_ab)
print("Product =", product_ab)
print("Square of a =", square_a)
print("Square of b =", square_b)


