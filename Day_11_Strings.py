# String Examples
name = "Chudamani"
lastName = 'Lawrence'
sentence = "Hello this is me typing the code here"

# Example of sentence string using double quotes inside single quote. Or vice versa can be done
another = 'He say, "I am the one who is builder and destroyer"'


# Multiline string
multiline = '''Hello this is an example of multiline string
This is another line of the multiline sting'''
print(multiline)

# We can access the characters of string using this technique
print(multiline[0]) # Accessing 0th element of the multiline variable
print(multiline[1])
print(multiline[2])
print(multiline[3])
print(multiline[4])
print(multiline[5])

# Looping through the string
for char in name:
  print(char)
for char in multiline:
  print(char)