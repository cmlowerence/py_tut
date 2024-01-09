# Shutil Module in Python
# ? Shutil is a Python module provides a higher level interface for working with files and directories. The name "shutil" is short for shell utility. It provides a convenient and efficient way to automate tasks that are commonly performed on files and directories. In the repl, we'll take a closer look at the shutil module and its various functions and how they can be used python

import shutil

# *Functions
#! The following are some of the most commonly used function in the shutil module:

# shutil.copy(src, dst) : #*The function copies the file located at arc to a new location specified by dst. If the destination location already exists, the original file will be overwritten.

# shutil.copy2(src, dst): #* This function is similar to shutil.copy, but it also preserves more metadata about the original file, such as the timestamp.

# shutil.copytree(src, dst): #* This function recursively copes the directory located at src to a new location specified by dst. If the destination location already exists, the original directory will be merged with it.

# shutil.move(src, dst): #*This function moves the file located at src to a new location specified by dst. This function is equivalent to renaming a file in most cases.

# shutil.rmtree(path): #*This function recursively deletes the directory located at path, along with all of its contents. This function is similar to using rm -rf command in a shell

# Examples

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
req_dir_files = ['src.txt', 'dst.txt', 'src_dir', 'dst_dir', 'src1.txt', 'dst1.txt', 'dir']

# Creating directories and files
for entry in req_dir_files:
  base_name, extension = os.path.splitext(entry)
  if extension:
    with open(entry, 'w'):
        pass
  else :
    os.makedirs(entry, exist_ok=True)


# Copying a file
shutil.copy('src.txt', 'dst.txt')

# Copying a directory
shutil.copytree('src_dir', 'dst_dir')

# Move a file
shutil.move('src.txt', 'dst.txt')

# Deleting a directory
shutil.rmtree('dir')