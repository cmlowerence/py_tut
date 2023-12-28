# opening a file
# ? Before we can perform any operations on a file, we must first open it. Python provides the open() function to open a file. It takes two arguments: the name of the file and the mode in which the file should be opened. The mode can be 'r' for reading, 'w' for writing, or 'a' for appending.

# Example
f = open('test.txt', 'r')
# * By default, the open() function returns a file object that can be used to read from or write to the file, depending on the mode

# Modes in file
# ? There are various modes i which we can open files
# * read (r) : This mode opens teh file for reading only and gives an error if the file does no exist. This is the default mode if no mode is passed as a parameter.
# * write(w): This mode opens the file for writing only and creates a new file if the file does not exist.
# *append (a): This mode opens the file for appending only and creates a new file if the file does not exist.
# * create (x): this mode creates a file and gives an error if the file already exists.
# *text (t): Apart from these modes, we also need to specify how the file must be handled. 't' mode is used to handle text files. 't' refers to text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (opening for reading text, synonym of 'rt')
# *binary (b): used to handle binary files (images, pdf s, etc)
# Reading from a file
f = open('test.txt','r')
contents = f.read()
print(contents)
f.close()


# Writing to a file
f = open('test.txt','w')
f.write('Chudamani is a great man!')
f.close()


# The 'with' statement
# ? Alternatively, we can use the with statement to automatically close the file after we are done working with it
# Example
with open('test.txt','r') as f:
  print(f.read())