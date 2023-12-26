# Python Dictionaries
# ? Dictionaries are ordered collection of data items. They store multiple items im a single variable. Dictionary item are key-value pairs that are separated by commas and enclosed within curly brackets{}
# Example
info = {'name':"Chudamani", "age":21, "eligible":True}
print(info)

# Q: Accessing Dictionary items

# Accessing single values:
# Values in dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in square brackets or by using get method
print(info['name'])
print(info.get('eligible'))


# Accessing multiple values
# We can print all the values in dictionary using values() method
print(info.values())

# Accessing keys:
# We can print all the keys in the dictionary using keys() method.
print(info.keys())

# Accessing key-value pairs:
# We can print all teh key-value pairs in the dictionary using items() method.
print(info.items())