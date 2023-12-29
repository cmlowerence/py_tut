# 'is' vs '==' in python
# ? In python, is and == are both comparison operators that can be used to check if two values are equal. However, there are some important differences between the two that we should be aware of.
  # * The 'is' operator compares the value of the objects. This means that 'is' will only return True if the object being compared are the exact same object in memory, while '==' will return True if the objects have the same value.
  
# Example
a = [1,2,3]
b = [1,2,3]
print(a == b) #! True
print(a is b) #! False

# ? In this case, a and b are two separate lists that have the same values, so == return True. However, a and b are not the same object in the memory, so 'is' returns False
  # ! One important thing to note is that, in Python, strings are integers are immutable, which means that once they are created, their values can't be changed. This means that, for string and integers, is and == will always return the same result
  
# Strings
a = 'Hello'
b = 'Hello'
print(a is b) # ! True
print(a == b) # ! True

# Numbers
a = 5
b = 5
print(a == b) #! True
print(a is b) #! True