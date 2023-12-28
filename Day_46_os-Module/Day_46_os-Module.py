# os Module in Python
# ? The os module in Python is built-in library that provides functions for interacting with the operation system. It allows us to perform a wide =variety of tasks, such as reading and writing files, interaction with the file system, and running system commands.
# Example
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) #! Changing path to current python file directory
# Open the file in read-only mode
f = os.open("test.txt", os.O_RDONLY)
# Read the contents of the file 
contents = os.read(f,1024)
# close the file
os.close(f)

# * To open a file for writing, we can use the os.O_WRONLY flag
# open file in write-only mode
f = os.open("test.txt",os.O_WRONLY)

# Write to the file
os.write(f, b"Hello, world! ")

# Closing the file
os.close(f)



# Interacting with the file system
# ? The os module also provides function for interacting with the file system. For example, we can use the os.listdir() function to get a list of the files in a directory
files = os.listdir(".")
print(files)

# we can even create a new directory using os.mkdir function
if (not os.path.exists("Chudamani")):
  os.mkdir("Chudamani")
# *Creating directories for our all python day courses
if (not os.path.exists("data")):
  os.mkdir("data")
for i in range(0,100):
  if (not os.path.exists(f"data/Day{i+1}")):
    os.mkdir(f"data/Day{i+1}")
for i in range(0,100):
  os.rename(f"data/Day{i+1}",f"data/Day {i+1}")