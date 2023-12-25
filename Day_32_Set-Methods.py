# Joining Sets
# ? Sets in python more or less work in the same way as sets in mathematics. We can perform operations like union and intersection on the sets just like in mathematics

# Q: union() and update()
# ? The union() and update() methods prints all items that are present in the two sets. The union() method returns a new set whereas update() method adds item into the existing set from another set.

# union()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)

# update()
cities.update(cities2)
print(cities)

# Q: intersection and intersection_update():
# ? The intersection() and intersection_update() methods prints only items that are similar to both the sets. The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.

# intersection()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities3 = cities.intersection(cities2)
print(cities3)

# intersection_update() 
cities.intersection_update(cities2)
print(cities)

# Q: symmetric_difference() and symmetric_difference_update()
# ? The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set

# symmetric_difference() 
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

# symmetric_difference_update()
cities.symmetric_difference_update(cities2)
print(cities)

# Q: difference() and difference_update():
# ? The difference() and difference_update() methods prints only items that are only present in the original set and not in both sets. The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.

# difference()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)

# difference_update()
cities.difference_update(cities2)
print(cities)

# Set Methods
print("Set Methods".center(40,"="))

# Q: isdisjoint()
# ? Checks weather item of given set are present in another set. Output in bool
# Example
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2)) #! False


# Q: issuperset():
# ? Checks if all teh items of a particular set are present in teh original set. Returns bool value
# Example
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
cities3 = {"Seoul", "Madrid", "Kabul"}
print(cities.issuperset(cities2)) #! False
print(cities3.issuperset(cities2)) #! True

# Q: issubset()
# ? Checks weather all teh items of the original set are present in the particular set. Returns bool value
# Example
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities)) #! True

# Q: add()
# ? to add a single item to set
# Example
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki") #! Adding element to set
print(cities)

# Q: update()
# ? To add more than one items. Just create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set
# Example
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)

# Q: remove()/discard()
# ? Use to remove item from the list
# Example
cities.remove("Tokyo")
print(cities)
# * discard() does the same thing but if the item is not present in the set, remove() method will raise an error while discard() will not.

# Q: pop()
# ? This method removes the last item of the set but teh catch is that we don't know which item gets popped as sets are unordered. However we can access the popped item if we assign the pop() method to a variable
# Example
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

# Q: del
# ? del is not a method, rather it is a keyword which deletes the set entirely
# Example
del cities
# print(cities) #! will throw error as cities variable is no longer there

# Q: clear()
# ? This method clears all items in the set and prints an empty set
# Example
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)


#todo Check weather item exist
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
  print("Carla is there in the set")
else:
  print("Carla is not there...")
