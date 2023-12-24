# To access a part of a string, we use string slicing
name = "Chudamani"
print(name[0:5]) # Printing the string characters from index 0 to 4

# TO find the length of a string we use len function
print(len(name))
print(f"My name contains {len(name)} characters")
# Slicing
print(name[0:])

# Negative slicing:
print(name[0:-2]) # short form for name[0:len(name) - 2]
print(name[0:len(name)-2])
print(name[-3:-1])

# Quick Quiz
nm = "Chudamani"
print(nm[-4:-2])