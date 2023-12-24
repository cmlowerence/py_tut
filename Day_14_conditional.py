# if...else statement
applePrice = 200
budget = 100
if (budget>=applePrice):
  print('You can buy this')
else:
  print(f"You have low money. You need additional ${applePrice-budget}")


# elif statement
# this is used for multiple condition checking in code
# Example
num = 0
if (num<0):
  print("Number is negative")
elif (num == 0):
  print("Number is Zero")
else:
  print("Number is positive")


# Nested if statement
# syntax
'''if(condition):
      code
    elif (condition):
      if(condition):
        code
      else:
        code
    else:
      code'''

num = 18
if (num<0):
  print("Number is negative")
elif (num>0):
  if(num<=10):
    print("Number is in between 1-10")
  elif(num>10 and num<=20):
    print("Number is in between 11-20")
  else:
    print("Number is greater than 20")
else:
  print("Number is Zero")