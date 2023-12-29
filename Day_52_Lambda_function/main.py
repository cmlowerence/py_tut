# Lambda Functions in python
# ?In python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following syntax:
# ! lambda arguments : expression

# ? Lambda functions are often used in situations where small function is required for a short period of time. They are commonly used as arguments to higher-order-functions, such as map, filter and reduce
# Example

# Function to double the input
def double(x):
  return x * 2

# Lambda function to double the input
print((lambda x : x * 2)(20))

# Lambda function can have multiple arguments, just like regular functions

# Function to calculate the product of two numbers
def multiply(x, y):
  return x * y

# Lambda function to calculate the product of two numbers
print((lambda x, y : x * y)(3,4))

# ! Lambda functions can also include multiple statements, but they ar limited to a single expression

# Lambda function to calculate the product of two numbers, with additional print statement
print((lambda x, y : print(f'{x} * {y} = {x * y}'))(5,7))

# We can store these functions in variables so that we can use them later
# Example
cube = lambda x : x ** 3 #! storing in variables
volume = lambda l, w, h : l * w * h

# using them
print(cube(10))
print(volume(4,5,6))