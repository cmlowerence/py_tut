list = [3,4,5,6]

# Accessing data form list
print(list[0]) # item at 0th index
print(list[1]) # item at 1th index
print(list[2]) # item at 2th index

# ! list are mutable
# adding element in list:
list.append(56)
print(list)

# Negative index
print(list[-3]) # negative index
print(list[-3]) # negative index
print(list[-3]) # negative index

# Checking weather a item is in list 
if 4 in list: # ! Using 'in' keyword
  print("Yes")
else:
  print("No")
  
# Printing all elements of list
print(list[:]) #! accessing all the elements
print(list[1:-1]) #! accessing element form index 1 to len(list)-1th index excluding that index element
print(list[::2]) #! Accessing all the elements but jumping 2 steps for next element or we can say, printing every second element of the list

# List comprehension
# ? generating list at instants like
lst = [i*i for i in range(1,5) if (i*i)%2==0]
print(lst)

# syntax
'''
List = [Expression(item) for item in iterable if condition]
Expression : It is the item which is being iterated
iterable: It can be list, tuples, dictionaries, sets, and even arrays and strings
Condition: Condition checks if teh item should be added to the new list or not
'''
# Example
names = ["Chudamani", "Rishi", "Virender", "Yuvraj", "Rakesh", "Rohit", "Rajesh", "Ramesh", "Cindy", "Ceaser", "Ariana"]
namesWith_o = [item for item in names if 'o' in item]
print(namesWith_o)