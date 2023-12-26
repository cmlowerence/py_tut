# Python- else in Loop
# ? Python allows the else keyword to be used with the for and while loops too. The else block appears after teh body of the loop. The statement in the while block will be executed after all iterations are completed. The program exits the loop only after teh else block is executed

# syntax
for counter in range(1):
  # Statements inside the for loop block
  pass
else:
  # statements inside else block
  pass

# Example:
for x in range(5):
  print("Iteration no {} in for loop".format(x+1))
else:
  print("Else block in loop")
print("Out of loop")