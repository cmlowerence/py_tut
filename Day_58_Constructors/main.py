# Constrictors
# ------------
# ? A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructors. Constructor is invoked automatically when an object of a class is created.

# A constructor is a unique function that gets called automatically when an object is created of a class. The main purpose of the constructor is to initialize or assign values to the data members of that class. It can't return any values other than None

# * Syntax of Python constructor
'''
#? def __init__(self):
    # Initializations
'''
# ! init is one of the reserved functions in Python. In Object Oriented Programming, it is known as a constructor.

# ? Types of Constructors in Python
# *1) Parameterized Constructor
# *2) Default Constructor

# Q: Parameterized Constructor in Python

# ? When the constructor accepts arguments along with self, it is knows as parameterized constructor.
# * These arguments can be used inside the class to assign the values to the data members.
# Example

class Details():
  def __init__(self, animal, group):
    self.animal = animal
    self.group = group
obj1 = Details("Crab", "Crustaceans")
print(f"{obj1.animal} belongs to the {obj1.group} group")

# Q: Default Constructor in Python
# Example
class Details:
  def __init__(self):
    print("Animal Crab belongs to Crustaceans group")
obj1= Details()
