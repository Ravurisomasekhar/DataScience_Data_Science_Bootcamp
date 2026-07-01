# # Module 5: Modules and Packages Assignments
# ## Lesson 5.1: Importing Modules
# ### Assignment 1: Importing and Using Modules
# Import the `math` module and use it to calculate the square root 
# of 25 and the sine of 90 degrees.

# import math
# print(math.sqrt(25))
# print(math.sin(math.radians(90)))


# ### Assignment 2: Aliasing Modules
# Import the `datetime` module with an alias and use it to print the current date and time.

# import datetime as dt
# print(dt.datetime.now())

# ### Assignment 3: Importing Specific Functions
# Import the `randint` function from the `random` module and use it to
#  generate a random integer between 1 and 100.

# from random import randint
# print(randint(1, 100))

# ### Assignment 4: Importing Multiple Functions
# Import the `sqrt` and `pow` functions from the `math` module and use
#  them to calculate the square root of 16 and 2 raised to the power of 3.

# import math
# print(math.sqrt(16))
# print(math.pow(2, 3))

# ### Assignment 5: Handling Import Errors
# Write code that attempts to import a non-existent module and gracefully handles 
# the import error by printing an error message.

# import importlib
# print("Attempting to import a non-existent module...")

# ## Lesson 5.2: Standard Library Overview
# ### Assignment 6: Working with the `os` Module
# Use the `os` module to create a new directory, list the contents of the current 
# directory, and remove the newly created directory.

# import os
# directory_name = "my_new_directory"

# # Create a new directory
# os.mkdir(directory_name)
# print(f"Directory '{directory_name}' created.")

# # List contents of the current directory
# print("\nContents of the current directory:")
# for item in os.listdir():
#     print(item)

# # Remove the newly created directory
# os.rmdir(directory_name)
# print(f"\nDirectory '{directory_name}' removed.")

# ### Assignment 7: Working with the `sys` Module
# Use the `sys` module to print the Python version currently in use 
# and the command-line arguments passed to the script.

# import sys

# # Print the Python version
# print("Python Version:")
# print(sys.version)

# # Print command-line arguments
# print("\nCommand-line Arguments:")
# print(sys.argv)

# ### Assignment 8: Working with the `math` Module
# Use the `math` module to calculate the greatest common divisor (GCD) of two 
# numbers and the factorial of a number.

# import math
# print(math.gcd(24,12))
# print(math.factorial(5))

# ### Assignment 9: Working with the `datetime` Module
# Use the `datetime` module to print the current date, calculate the date 100 
# days from today, and determine the day of the week for a given date.

# import datetime

# currernt_date = datetime.date.today()
# print("Current Date:", currernt_date)
# print("Date 100 days from today:", currernt_date + datetime.timedelta(days=100))

# ### Assignment 10: Working with the `random` Module
# Use the `random` module to generate a list of 5 random numbers between 1 and 50 
# and shuffle the elements of a list.

# import random
# print(random.sample(range(1, 51), 5))
# print(type(random.sample(range(1, 51), 5)))

# ## Lesson 5.3: Creating and Using Packages
# ### Assignment 11: Creating a Simple Package
# Create a package named `mypackage` with two modules: `module1` and `module2`. `module1`
#  should contain a function that adds two numbers, and `module2` should contain a function 
# that multiplies two numbers. Write code to use these functions.


# no able solve it 












# ### Assignment 12: Using `__init__.py`
# Modify the `mypackage` package to include an `__init__.py` file that imports the functions from `module1` and `module2`. Write code to use these functions.













# ### Assignment 13: Importing from a Package
# Write code to import and use the functions from `mypackage` without explicitly importing `module1` and `module2`.







# ### Assignment 14: Relative Imports
# Create a subpackage named `subpackage` within `mypackage` and move `module2` into `subpackage`. Modify the import statements in `__init__.py` to use relative imports. Write code to use the functions from both modules.






# ### Assignment 15: Handling Package Import Errors
# Write code that attempts to import a non-existent function from `mypackage` and gracefully handles the import error by printing an error message.
