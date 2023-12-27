# Finally Clause
# ? The finally code block is also a prat of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.

# Syntax
try:
  #statement that could generate error
  pass
except:
  # solution of generated exception
  pass
finally:
  # block of code which is going to execute in any situation
  pass


# The finally block is executed irrespective of the outcome of try...except...else blocks
# One of the important use cases of finally block is in a function which return a value

# Example:
try:
  num: int(input("Enter an integer: "))
except ValueError:
  print("Number entered is not an integer.")
finally:
  print("This block is always executed")