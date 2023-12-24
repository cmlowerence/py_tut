a = "Chudamani"
print(len(a))
# ! String are immutable, means we can't change them directly
# Q: Changing to Uppercase
print(a.upper())
print(a.lower()) # changing to lower case
# todo: The real string is not changed. A copy of the main string is generated and operations are on them

# Q: rstrip() string method
str = "Oh my! god!!! my!"
print(str.rstrip('!')) # all trailing characters matching ! will get stripped

# Q: replace() string method
print(str.replace('my!',"Our!")) # ! All occurrence matching first argument will be changed by second argument of replace() method

# Q: split() string method
print(str.split(" ")) # ! In this method, we can split any string from a specific point given in argument

# Q: capitalize() function
newStr = 'chudamani is a good man. once one man goes from ome'
print(newStr.capitalize()) # first letter of string gets capitalize

# Q: center() method
centerStr = 'This is a test string'
print(centerStr.center(100))
print(len(centerStr))
print(len(centerStr.center(100))) # this method centers the string adding white spaces
# we can add some special character in place of whitespaces by giving them in second argument of the method like:
print(centerStr.center(50,'.'))

# Q: count() method ! this method counts the occurrence of argument given in count() method in the operating string
countStr = 'This is test string which is doing some stuff'
print(countStr.count('is')) # ! this method counts the all occurrence of the argument given in the whole string irrespective of word

# Q: endswith() method {this methods checks weather the operating string ends with the argument given is the endswith() method}
endsWithStr = 'This is a test string'
print(endsWithStr.endswith('is')) #! False
print(endsWithStr.endswith('string')) #! True
# we can also check for a value in-between the string by providing start and end index position
print(endsWithStr.endswith('is',4,7)) # ! this will check weather this slice of string ends with the given method argument

# Q: find() method: {this find() method searches for teh first occurrence of a given value and returns the index where it is present. If given value is absent from teh string then return -1}
findStr = 'Hello there my name is hero hira lal'
print(findStr.find('my')) # ! return index of first occurrence of 'my' in findStr
print(findStr.find('chudamani')) # ! gives -1 as 'chudamani is not present in findStr

# Q: index() method
# ? The index method searches for the first occurrence of the given value and return the index where it is present. If given value is absent from the string then raise an exception
indexStr = 'Hello there'
print(indexStr.index('h')) #! will raise an exception as 'ro' is not present in indexStr
# Other than this, this method is same as find() method

# Q: isalnum() method
# ? The isalnum() method returns 'True' only if the entire string only consists of A-Z,a-z,0-9. If any other characters or punctuations are present, then it return 'False'
sampleStr = 'WelcomeToTheConsole123'
print(sampleStr.isalnum()) #! True as no other character are there

# Q: isalpha() method
# ? isalpha() methods return 'True' only if the entire string only consists of A-Z, a-z. If any other Character or punctuations or numbers (0-9) are present then return 'False'
print(sampleStr.isalpha()) #! False, as numbers are also present in sampleStr

# Q: islower() method
# ? The islower() method return True if all the characters in the string are lower case, else it returns False
lowerStr = 'hey there'
properStr = 'Hey There'
print(lowerStr.islower()) #! True as all the characters are in lower case
print(properStr.islower()) #! False as all the characters are'n in lower case

# Q: isprintable() method
# ? The isprintable() method return True if all the values within the given string are printable if not, then return False
printableStr = 'We wish you all a Merry Christmas'
print(printableStr.isprintable()) #! True

# Q: isspace() method
# ? The isspace() method return 'True' only and only if the string contains white spaces, else returns 'False'
spaceStr = "    "
print(spaceStr.isspace()) #! True as string only contains spaces

# Q: istitle() method
# ? The istitle() returns True only if the first letter of each word of the string is capitalized, else False
titleStr = 'World Health Organization'
nonTitleStr = 'My name'
print(titleStr.istitle()) #! True
print(nonTitleStr.istitle()) #! False

# Q: isupper() method
# ? The isupper() method returns True if all the characters in the string are upper case, else it returns False
upperStr = 'THIS STRING IS AN UPPER CASE STRING'
print(upperStr.isupper()) #! True

# Q: startswith() method
# ? The startswith() method checks if the string starts with a given value. If yes then True else False
startString = 'Python is a funny language'
print(startString.startswith('Python')) #! True
print(startString.startswith('language')) #! False

# Q: swapcase() method
# ? The swapcase() methods changes the character of the string. Uppercase are converted to lowercase and lower case to uppercase
swapStr = 'Python is a Funny Language'
print(swapStr.swapcase())#! pYTHON IS A fUNNY lANGUAGE

# Q: title() method
makeTitleStr = 'world health organization'
print(makeTitleStr.title()) #! World Health Organization
