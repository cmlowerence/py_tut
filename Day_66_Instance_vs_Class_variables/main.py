# Instance vs class variables
# ? In python, variable can be defined at the class level or at the instance level. Understanding the difference between these types of variables is crucial for writing efficient and maintainable code

# Q: Class Variable
# ? Class variables are defined at the class level and are shared among all instances of the class. They are defined outside of any method and are usually used to store information that is common to all instances of the class. For example, a class variable can be used to store the number of instances of a class that have been created

class MyClass:
  class_variable = 0
  def __init__(self):
    MyClass.class_variable +=1
  def print_class_variable(self):
    print(MyClass.class_variable)

obj1 = MyClass()
obj2 = MyClass()
obj2 = MyClass()
obj2 = MyClass()

obj1.print_class_variable()
obj2.print_class_variable()

# Instance Variables
# ? Instance variables are defined at the instance level and are unique to each instance of the class. They are defined inside the init method and are usually used to store information that is specific to each instance of the class. For example, an instance variable can be used to store the name of an employee in a class that represents an employee

# Example
class MyClass1:
  def __init__(self, name):
    self.name = name
  def print_name(self):
    print(self.name)
    
obj1 = MyClass1("John")
obj2 = MyClass1("Joe")
obj1.print_name()
obj2.print_name()