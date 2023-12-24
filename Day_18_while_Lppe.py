# Python while loop
count = 5
while (count > 0):
  print(count)
  count -= 1

# Else with while loop
# we can use else statement with the while loop. Essentially what the else statement dos is that as soon as the while loop condition becomes False, the interpreter comes out of the while loop and the else statement is executed
x = 5
while (x > 0):
  print(x)
  x -= 1
else:
  print("Value of x is zero now")
  
# Emulation of do-while loop in python
# do...while loop is a loop in which a set of instructions will executed at least once (irrespective of the condition) and then the repetition of loop's body will depend on the condition passed at the end of teh while loop. It is also known as an exit-controlled loop.

while True:
  number = int(input('Enter a positive number: '))
  print(number)
  if not number > 0:
    break