# Python Decorators
# ? Python decorators are powerful and versatile tool that allows us to modify the behavior of teh function and method. They are a way to extend the functionality of function without modifying its code.

# * A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as 'decorated" function. The basic syntax using a decorator is 

decorator_function = lambda x : print("This is decorator_function body")
@decorator_function
def my_function():
  #! function body
  pass

# The @decorator_function is notation is just a shorthand for the following code
def my_function():
  print("This is my_function body")
  pass
my_function = decorator_function(my_function)


# Decorators are often used to add functionality to functions and methods, such as logging, memorization, and access control

# ? Practical use case
# *One common use of decorators is to add logging to a function.
# For example, we could use a decorator to log the arguments and return values of a function each time it is called:
import logging

def log_function_call(func):
  def decorated(*args,**kwargs):
    logging.info(f"Calling {func.__name__} with args={args}, kwargs = {kwargs}")
    result = func(*args,**kwargs)
    logging.info(f"{func.__name__} returned {result}")
    return result
  return decorated

@log_function_call
def my_function(a,b):
  return a + b
print(my_function(1,2))




def my_decorator(func):
  def decorated(*args, **kwargs):
    print("Program Initiated...")
    val = func(*args, **kwargs)
    print("Program terminated...")
    return val
  return decorated

@my_decorator
def add (a, b):
  print(a+b)

add(10,10)