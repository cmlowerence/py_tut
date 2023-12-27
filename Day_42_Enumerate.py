# Enumerate function in python
# ? The enumerate function is a built-in function in python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time. Here's a basic example of how it works:

# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
  print(index,fruit)

# As we can see, the enumerate function returns a tuple containing the index and value of each element in the sequence. We can use the for loop to unpack these tuples and assign them to variables, as above

# * Changing the start index
# ? By default, the enumerator function starts the index at 0, but we can specify a different starting index by passing it as an argument to the enumerate function.
# Loop over a list and print the index starting at 1 and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
  print(f"{index}: {fruit}")
  
  
# * Using enumerate function on tuple
# Loop over a tuple and print the index and value of each element
colors = ('red', 'green', 'blue')
for index, color in enumerate(colors):
  print(f"{index}: {color}")
  
# * Using enumerate function on string
# Loop over a string and print the index and value of each character
s = 'hello'
for index, char in enumerate(s):
  print(index,char)