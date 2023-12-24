# syntax
'''
match variable_name:
  case "pattern1":
    statement 1
  case "pattern2":
    statement 2
  ...
  case "pattern_n:
    statement n
  '''

# Example
x = int(input("Enter the value of x: "))
# x is a variable ot match
match x:
  # if x is 0
  case 0:
    print(f"{x} is Zero")
  # case with if condition
  case 4 if x % 2 == 0:
    print(f"{x} % 2 == 0 and case if 4")
  # Empty case with if condition
  case _ if x<10:
    print(f"{x} is < 10")
  # default case (will only be matched if the above cases were not matched)
  case _: # _ is for default case indication
    print(x)

# ! No need for break statement like other switch case statements