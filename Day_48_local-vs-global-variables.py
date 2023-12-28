# local and global variables
# ? A local variable is a variable that is defined within a function and is only accessible within that function. It is created when the function is called and is destroyed when a function returns
  # * On the other hand, a global variable is a variable that is defined outside of a function and is accessible from within any function in our code
  
x = 10 # global variable

def my_function():
  y = 5 # local variable
  print(y)
  print(x)
my_function()
print(x)
# print(y) #! This will raise error
# In this example, we have a global variable x and a local variable y. We can access the value of the global variable x from within the function, but we can't access teh value of the local variable y outside of the function.


# * The global keyword
# ? Now, what if we want to modify a global variable from within a function? This is where the global keyword comes.
# * The global keyword is used to declare that a variable is a global variable and should be accessed from the global scope.

x = 10 # global variable
def my_function1():
  global x
  x = 5 # This will change teh value of the global variable x
  y = 5
my_function1()
print(x)