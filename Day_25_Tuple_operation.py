# Manipulating Tuples
# ? Tuples are immutable, hence if we want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries) #Changing tuple into list
temp.append("Russia")#Adding item to the temp list
temp.pop(3) #Removing an item
temp[2] = "Finland" #Changing item
countries = tuple(temp)
print(countries)


# Tuple methods
# ? As tuple is immutable type of elements, it have limited built in methods.

# Q: count() method
# ?The count() method of TUple returns the number of times the given element appears in the tuple
tuple1 = (0,1,2,3,2,3,1,3,2)
res = tuple1.count(3)
print("Count of 3 in tuple1 is :",res)

# index() method
# ? The index() method returns the first occurrence of the given element from the tuple
# * syntax: tuple.index(element,start,end)
# if value is not found in the tuple, it will raise a valueError
tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = tuple.index(3)
print('First occurrence of 3 is ',res)