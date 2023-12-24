# Two types of loops
# * for loop
# * while loop

# ? For loop
# This loop can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iteration over string, lists, tuples, sets and dictionaries

# * iterating over string
name = "Chudamani"
for char in name:
  print(char,end=", ")
print()
# *iterating over list
colors = ["Red","Green","Blue","Yellow"]
for color in colors:
  print(color)

# range()
# if we do not want to iterate over a sequence then we use range() function like:
for num in range(5):
  print(num)
# We can even loop over a specific range
for num in range(4,9):
  print(num)

# We can even give step breaks in the range series by giving third parameter in range() function
print()
for num in range(0,10,2):
  print(num)