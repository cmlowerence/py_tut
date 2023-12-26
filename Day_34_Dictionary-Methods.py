# Dictionary Methods

# Dictionary uses several built-in methods for manipulating. They are listed below

# Q: update()
# ? The update() method updates the value of the key provided to it if the item already exist in the dictionary, else it creates a new key-value pair.
# Example
info = {'name':'Chudamani', 'age': 19, 'eligible': True}
print(info)
info.update({'age': 21}) #! updating the value of age from 19 to 21
info.update({'DOB' : 2003}) #! As DOB is not present, it will be the next key-value pair of dictionary
print(info)

# Removing items fro dictionary

# Q: clear()
# ? The clear() method removes all teh items from the list
# Example 
info.clear()
print(info)

# Q: pop():
# ? The pop() method removes teh key-value pair whose key is passed as a parameter

info = {'name': 'Chudamani', 'age': 21, 'eligible': True}
info.pop('eligible')
print(info)

# Q: popitem():
# ? The popitem() method removes the last key-value pair from the dictionary
# Example
info.update({'eligible':True})
info.update({'DOB': 2003})
info.popitem()
print(info)

# Q: del:
# ? We can also use the del keyword to remove a dictionary item
info.update({'DOB':2003})
del info['age'] #* Deletes the 'age' key of the info dictionary
print(info)
# del info #* Deletes the info variable by whole
# print(info) #! Will throw an error