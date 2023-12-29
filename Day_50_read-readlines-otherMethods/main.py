
# Q: readlines() method
# ? The readline() method reads a single line from the file. If we want to read multiple ines, we can use a loop
# Example
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open('test.txt','r') as f:
  while True:
    line = f.readline()
    if not line:
      break
    print(line)
# * The readlines() method reads all the lines of the file and returns them as a list of strings.
with open ('test.txt','r') as f:
  print(f.readlines())
  
# Q: writelines() method
# ? The writelines() method in Python writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple
# Example
with open ('myfile.txt','w') as f:
  lines = ['line1\n','line2\n', 'line3\n']
  f.writelines(lines)
with open ('myfile.txt','r') as f:
  print(f.readlines())
  
# ? This will write teh strings in the lines list to the file myfile.txt. The \n characters are used to add new line characters to the end of each string.
# * The writelines() method doesn't add newline characters between the strings in the sequence. If we want to add newlines between teh strings, we can use a loop to write each string separately:
with open ('myfile.txt','w') as f:
  lines = ['line 1', 'line 2', 'line 3']
  for line in lines:
    f.write(line + '\n')
with open ('myfile.txt','r') as f:
  print(f.readlines())