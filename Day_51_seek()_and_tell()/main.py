import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Q: seek() and tell() functions
# ? In python, the seek() and tell() functions are used to work with file objects and their positions within a file. These functions are part of the built-in IO module, which provides a consistent interface for reading and writing to various file like objects, such as files, pipes, and in-memory buffers.

# * seek() function
# The seek() function allows us to move the current position within a file to a specific point. The position is specified in bytes, adn we can move either forward or backward from the current position
with open ('file.txt','r') as f:
  # Move to 10th byte in the file
  f.seek(10)
  data = f.read(6) # Read the next 5 bytes
  print (data)
  
# * tell() function
# The tell() function returns the current position within the file, in bytes. This can be useful for keeping track of our location within the file or for seeking to a specific position relative to current position
with open ('file.txt','r') as f:
  # Read teh first 10 bytes
  data = f.read(10)
  print("Normal".center(40,'='))
  print(data)
  
  # Save the current position
  current_position = f.tell()
  
  # Seek to the saved position
  f.seek(current_position)
  print("After seeking".center(40,'='))
  print(f.read())


# * truncate() function
# When we open a file in python using the open function, we can specify the mode in which we want to open the file. If we specify the mode as 'w' or 'a', the file is opened in write mode and we can write to the file. However, if we want to truncate the file to a specific size, we can use the truncate function

with open ('sample.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(5)
  
with open('sample.txt', 'r') as f:
  print(f.read())