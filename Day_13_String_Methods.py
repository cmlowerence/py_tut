a = "Chudamani"
print(len(a))
# ! String are immutable, means we can't change them directly
# Changing to Uppercase
print(a.upper())
print(a.lower()) # changing to lower case
# todo: The real string is not changed. A copy of the main string is generated and operations are on them

# rstrip() string method
str = "Oh my! god!!! my!"
print(str.rstrip('!')) # all trailing characters matching ! will get stripped

# replace() string method
print(str.replace('my!',"Our!")) # ! All occurrence matching first argument will be changed by second argument of replace() method

# split() string method
print(str.split(" ")) # ! In this method, we can split any string from a specific point given in argument

# capitalize() function
newStr = 'chudamani is a good man. once one man goes from ome'
print(newStr.capitalize()) # first letter of string gets capitalize

# center() method
centerStr = 'This is a test string'
print(centerStr.center(100))
print(len(centerStr))
print(len(centerStr.center(100))) # this method centers the string adding white spaces

# count() method ! this method counts the occurrence of argument given in count() method in the operating string
countStr = 'This is test string which is doing some stuff'
print(countStr.count('is')) # ! this method counts the all occurrence of the argument given in the whole string irrespective of word

# endswith() method {this methods checks weather the operating string ends with the argument given is the endswith() method}
endsWithStr = 'This is a test string'
print(endsWithStr.endswith('is')) #! False
print(endsWithStr.endswith('string')) #! True
