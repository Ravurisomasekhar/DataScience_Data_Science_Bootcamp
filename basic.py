# # Lesson 1.2: Python Basics
# ## Topics Covered:
# - Syntax and Semantics
# - Variables and Data Types
# - Basic Operators (Arithmetic, Comparison, Logical)

# ## 1. Syntax and Semantics

# **Question 1:** Write a Python program to print "Hello, World!".
# # Your code here

# anmwers :

# print("Hello, World!")


# **Question 2:** Write a Python program that takes a user input and prints it.
# # Your code here

# answer: 

# n = input()
# print(n)


# **Question 3:** Write a Python program to check if a number is positive, negative, or zero.
# # Your code here

# answer : 

# n = input()
# if n  === 0:
#     print("zero")
# elif n% 2 == 0:
#     print("Positive")
# else:
#     print("Negative")


# **Question 4:** Write a Python program to find the largest of three numbers.
# # Your code here

# answer :

# Take three numbers as input
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# # Find the largest number
# if a >= b and a >= c:
#     largest = a
# elif b >= a and b >= c:
#     largest = b
# else:
#     largest = c

# print("The largest number is:", largest)

    
# **Question 5:** Write a Python program to calculate the factorial of a number.
# # Your code here
# ## 2. Variables and Data Types

# n = int(input())

# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
# print(fact)



# **Question 6:** Create variables of different data types: integer, float, string, and boolean. Print their values and types.
# Your code here


# Integer
# age = 24

# # Float
# height = 5.8

# # String
# name = "Somasekhar"

# # Boolean
# is_student = True

# # Print values and their types
# print("Value:", age, "| Type:", type(age))
# print("Value:", height, "| Type:", type(height))
# print("Value:", name, "| Type:", type(name))
# print("Value:", is_student, "| Type:", type(is_student))

# **Question 7:** Write a Python program to swap the values of two variables.
# # Your code here

# a = 5
# b = 10

# a,b = b,a
# print(a,"a")
# print(b,"b")


# **Question 8:** Write a Python program to convert Celsius to Fahrenheit.
# # Your code here

# Celsius to Fahrenheit Conversion
# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print("Temperature in Fahrenheit:", fahrenheit)


# **Question 9:** Write a Python program to concatenate two strings.
# # Your code here

# Concatenate two strings

# string1 = input("Enter first string: ")
# string2 = input("Enter second string: ")
# result = string1 + string2
# print("Concatenated String:", result)

# **Question 10:** Write a Python program to check if a variable is of a specific data type.
# # Your code here
# ## 3. Basic Operators (Arithmetic, Comparison, Logical)

# intget DataType
# Check if a variable is of a specific data type

# x = 10

# if isinstance(x, int):
#     print("x is of type int")
# else:
#     print("x is not of type int")

# ====================================

# name = "Somasekhar"

# if isinstance(name, str):
#     print("name is a string")


# **Question 11:** Write a Python program to perform arithmetic operations: addition, subtraction, multiplication, and division.
# # Your code here

# Perform arithmetic operations

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# print("Addition:", num1 + num2)
# print("Subtraction:", num1 - num2)
# print("Multiplication:", num1 * num2)
# print("Division:", num1 / num2)


# **Question 12:** Write a Python program to demonstrate comparison operators: equal to, not equal to, greater than, less than.
# # Your code here

# Demonstrate comparison operators

# a = 10
# b = 5

# print("a == b :", a == b)  # Equal to
# print("a != b :", a != b)  # Not equal to
# print("a > b  :", a > b)   # Greater than
# print("a < b  :", a < b)   # Less than

# **Question 13:** Write a Python program to demonstrate logical operators: and, or, not.
# # Your code here

# a = 10
# b = 5

# print("AND Operator:", a > 5 and b < 10)
# print("OR Operator :", a < 5 or b < 10)
# print("NOT Operator:", not(a > 5))

# **Question 14:** Write a Python program to calculate the square of a number.
# # Your code here

# num = float(input("Enter a number: "))
# square = num ** 2
# print("Square of the number is:", square)

# **Question 15:** Write a Python program to check if a number is even or odd.
# # Your code here

# n = int(input())
# if n%2 == 0:
#     print("Even")
# elif n%2 != 0:
#     print("Odd")

# **Question 16:** Write a Python program to find the sum of the first n natural numbers.
# # Your code here

# Find the sum of the first n natural numbers

# n = int(input("Enter a number: "))
# sum_n = n * (n + 1) // 2
# print("Sum of first", n, "natural numbers is:", sum_n)


# **Question 17:** Write a Python program to check if a year is a leap year.
# # Your code here

# Check if a year is a leap year

# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(year, "is a Leap Year")
# else:
#     print(year, "is not a Leap Year")

# **Question 18:** Write a Python program to reverse a string.
# # Your code here

# n = input()
# print(n[::-1])


# **Question 19:** Write a Python program to check if a string is a palindrome.
# # Your code here

# n = input()
# print(n == n[::-1])

# **Question 20:** Write a Python program to sort a list of numbers in ascending order.
# # Your code here

# lst = [5, 2, 9, 1, 5, 6]
# print(sorted(lst))

# final coding part