# Recursion in python
# ? Recursion is the process of defining something in terms of itself

# ! Python Recursive Function
# ? In python, e know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions

# * Finding factorial using recursion
def fact(num):
  if (num == 1 or num == 0):
    return 1
  else:
    return num * fact(num-1)
num = int(input("Enter the number: "))
print(f"The factorial of {num} is {fact(num)}")