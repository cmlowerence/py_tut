# The Walrus Operator in Python
# ? The Walrus Operator is a new addition in Python 3.8 and allow us to assign a value to a variable within an expression. THis can be useful when we need to use a value multiple times in a loop, but don't want to repeat the calculation
# * The Walrus Operator is represented by := syntax and can be used in variety of contexts including while loops and if statements.
# Example
numbers = [1,2,3,4,5]

while (n := len(numbers)) > 0:
  print(numbers.pop())
print(numbers)

# Another example
names = ["John", "Jane", "Jim"]

if (name := input("Enter a name: ")) in names:
  print(f"Hello, Welcome {name}")
else:
  print(f"Access Denied for {name}")
  
happy = True
print(happy)

print(happy := False)

foods = list()

# Not using walrus operator
# while True:
#   food = input("What food do you like?: ")
#   if food == "quit":
#     break
#   foods.append(food)
  
# ! using walrus operator
while (food := input("What food do you like?: ")) != "quit":
  foods.append(food)
print(foods)