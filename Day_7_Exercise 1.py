# Create a calculator which is capable of performing addition, subtraction, multiplication and division operations on two numbers. Your program should format the output in a readable manner
print(f"Enter + for addition\nEnter - for subtraction\nEnter * for multiplication\nEnter / for division")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("What to do: ")
if (operation == '+'):
  print(f"Sum of {num1} and {num2} is {num1 + num2}")
elif (operation == '-'):
  print(f"Difference of {num1} and {num2} is {num1 - num2}")
elif (operation == '*'):
  print(f"Product of {num1} and {num2} is {num1 * num2}")
elif (operation == '/'):
  print(f"Division of {num1} by {num2} is {num1 / num2}")
else:
  print("Wrong operation sign...")
