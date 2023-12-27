# Raising Custom errors
# ? In python, we can raise custom erros by using the 'raise' keyword
salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
  raise ValueError("Not a Valid salary.")

# ? In the previous tutorial, we learned about different built-in exceptions in Python and why it is important to handle exceptions. However, sometimes we may need to create our own custom exceptions that serve our purpose.

# Defining Custom Exceptions
# ? In the Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class
# Example
class CustomError(Exception):
  # ...code
  pass
try:
  # ...code
  pass
except CustomError:
  #...code
  pass


