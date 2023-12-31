# Python Class and Objects
# ? A class is a blueprint or template for creating objects, providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods). The user-defined objects are created using the class keyword.

# Q: Creating a Class:
# Example
class Details:
  name = "Chudamani"
  age = 20

# Q: Creating a Object:
# ? Object is the instance of the class used to access the properties of the class.
# Example
obj1 = Details() #! Object

# printing values
print(obj1.name)
print(obj1.age)

# self parameter
# ? The self parameter is a reference to the current instance of teh class, and is used to access variables that belongs to the class.
# Example
class Details:
  name = "Chudamani"
  age = 21
  IQ = 200
  def desc(self):
    print(f"My name is {self.name}, and I'm {self.age} years old. My IQ is {self.IQ}.")
    
obj1 = Details()
obj1.desc()
obj2 = Details()
obj2.name = "Rohit"
obj2.age = 50
obj2.IQ = 60
obj2.desc()