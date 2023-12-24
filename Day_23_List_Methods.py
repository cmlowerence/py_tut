# List Methods

# Q: list.sort()
# ? This method sorts the list in ascending order. The original list is updated
# Example

# In string
colors = ["violet","indigo","blue","green"]
print(colors)
colors1 = [color for color in colors]
colors.sort() # Sorting alphabetically
print(colors)

# In numbers
num = [4,3,5,1,6,1,3,9,6,4,7]
print(num)
num1 = [num for num in num]
num.sort() #sorting in ascending order
print(num)

# Sorting in descending order
colors1.sort(reverse=True)
print(colors1)
num1.sort(reverse=True)
print(num1)


# Q: reverse() method
# ? This method reverses the order of the list
colors2 = ["violet","indigo","blue", "green"]
colors2.reverse()
print(colors2)

num2 = [4,2,5,3,6,1,2,1,2,8,9,7]
num2.reverse()
print(num2)

# Q: index()
# ? This method returns the index of the first occurrence of the list item
colors3 = ["violet", "green", "indigo", "blue", "green"]
print(colors3.index("green"))

num3 = [4,2,5,3,6,1,2,1,2,8,9,7]
print(num3.index(3))

# Q: count()
# ? Returns the counts to the number of items with the given values
colors = ["violet", "green", "indigo", "blue", "green"]
print(colors.count("green"))
num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.count(2))

# Q: copy()
# ? Returns copy of the list. This can be done to perform operations on the list without modifying the original list
colors = ["violet", "green", "indigo", "blue"]
newList = colors.copy()
print(colors)
print(newList)


# Q: insert()
# ? This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method
colors = ["violet", "indigo", "blue"]
colors.insert(1,"green")
print(colors)

# Q: extend()
# ? This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.
colors = ["violet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)
# ! Printing first character of each index
for clr in colors:
  print(clr[0].upper())