# Regular Expression in Python

# ? Regular expressions, or "regex" for short, are a powerful tool for working with strings and text data in Python. They allow you to match and manipulate strings based on patterns, making it easy to perform complex string operations with just a few lines of code.

# Metacharacters in regular expression

'''
[]  Represent a character class
^   Matches the beginning
$   Matches the end
.   Matches any character except newline
?   Matches zero or one occurrence.
|   Means OR (Matches with any of teh characters separated by it)
*   Any number of occurrences (including 0 occurrences)
+   One or more occurrences
{}  Indicate number of occurrences of a preceding RF to match
()  Enclose a group of REs
'''

# Importing re package
# ? In Python, regular expressions are supported by the re module. The basic syntax for working with regular expressions in Python 
import re

# Searching for a pattern in re using re.search() Method

pattern = r"H"

text = "Hello, World!"
match =re.search(pattern, text)
if match:
  print("Match Found")
else:
  print("No match found")

# searching for a pattern in re using re.findall() Method

pattern = r"[a-z]+at"
text = "The cat is in the hat"
matches = re.findall(pattern, text)
print(matches)

# replacing the matching text
pattern = r"[a-z]+at"
new_text = re.sub(pattern, "dog", text)
print(new_text)

# Extracting information from the strings
text = "The email address is cmlowerence2777@gmail.com."

pattern = r"\w+@\w+\.\w+"

matches = re.search(pattern, text)
if matches:
  email = matches.group()
  print(email)
else:
  print("No match found")
  
  