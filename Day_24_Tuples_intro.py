# Python Tuples
# ? Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we can't alter them after creation

# Example
tuple1 = (1,2,3,4,5,6,7,8,9)
tuple2 =  ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)
print(type(tuple1),type(tuple2))

# Example
details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details)

# Tuple indexes
country = ("Spain", "Italy", "India")

# Accessing tuple items
print(country[0]) #! Same as lists
print(country[1]) #! Same as lists
print(country[2]) #! Same as lists

# negative indexing
country = ("Spain", "Italy", "India", "England", "Germany")
print(country[-1])
print(country[-2])
print(country[-3])
print(country[-4])

# Q: Check for an item
# ? we can use in keyword for that
if "Germany" in country:
  print("Germany is safe")
else:
  print("Germany is no longer a country")

# Range of Index
# ?Syntax: Tuple[start: end: JumpIndex]
# Example
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7]) # Positive index
print(animals[-7:-2]) #negative index
print(animals[:]) # Printing all the elements
print(animals[1::2]) # Printing every second element from index 1 to end index