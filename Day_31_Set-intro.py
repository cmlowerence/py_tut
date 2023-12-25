# Python Sets
# ? Sets are unordered collection of data items. They store multiple items in a single variable. Set items are separated by commas and enclosed within curly brackets{}. Sets are unchangeable, meaning we can't change items of teh set once created. 
#!Sets do not contain duplicate items.

# Example
info = {"Carla", 19, False, 5.9, 19}
print(info) #! {False, 'Carla', 19, 5.9}
#* Here we can see that set values comes in different order as assigned, so we can't access them using their index numbers. Also duplicate values are omitted by the set

# todo: Accessing set items
# * Using for loop
for item in info:
  print(item)