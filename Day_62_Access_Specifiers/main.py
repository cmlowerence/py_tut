# Access Specifiers/Modifiers
# ? Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance

# Q: Types of access specifiers
# 1) Public access modifier
# 2) Private access modifier
# 3) Protected access modifier


# Q: Pubic Access Specifier in Python
# ? All the variables and methods (members function) in python are by default public. Any instance variable in a class followed by the 'self' keyword i.e. self.var_name are public accessed
# Example
class Student:
  # constructor id defined
  def __init__(self,age,name):
    self.age = age   # Public variable
    self.name = name # Public variable
    
obj = Student(21,"Chudamani")
print(obj.age)
print(obj.name)


# Q: Private access specifier in python
# ? By definition, Private members of a class (variables or methods) are those members which are only accessible inside the class. We can't use private members outside of class

# In Python, there is no strict concept of "private" access modifiers like in some other programming languages. However, a convention has been established to indicate that a variable or a methods should be considered private by prefixing its name with a double underscore(__). This is known as "weak internal use indicator" and it is a convention only, not a strict rule. Code outside the class can still access these "private" variables and methods, but is generally understood that they should not be accessed or modified

# *Example
class Student:
  def __init__(self,age,name):
    self.__age = age # An indication of private variable
  def __funcName(self): # An indication of private function
      self.y = 34
      print(self.y)
class Subject(Student):
  pass

obj = Student(21, "Chudamani")
obj1 = Subject
# Calling by object of class Student
# print(obj.__age)
# print(obj.__funcName) #Will raise error 


# Q: Name mangling
# ? Name mangling in Python is a technique used to protect class-private and superclass-private attributes from being accidentally overwritten by subclasses. Names of class-private and superclass-private attributes are transformed by the addition of a single leading underscore and a double leading underscore respectively
# Example
class MyClass:
  def __init__(self):
    self._non_mangled_attribute = "This is non_mangled attributed"
    self.__mangled_attribute = "I am a mangled attribute"
my_obj = MyClass()
print(my_obj._non_mangled_attribute) # Output is shown
# print(my_obj.__mangled_attribute) # ! Throws an error
print(my_obj._MyClass__mangled_attribute) # Will give output now


# Q: Protected Access Modifiers

# ? In OOP, the term "protected" is used to describe a member (i.e. a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses. In python, the convention for indicating that a member is protected is to prefix its name with a single underscore(_). For example, if a class has a method called _my_method, it is indicating that the method should only be accessed by the class itself and its subclasses

# * It's important to note that the single underscore is just a naming convention, and does not actually provide any protection or restrict access to the member. The syntax we follow to make any variable protected is to write variable name followed by a single underscore (_) i.e. _varName
# Example
class Student:
  def __init__(self):
    self._name = "Harry"
  def _funcName(self):
    return "CodeWithHarry" #protected method
  
class Subject(Student):
  pass
obj = Student()
obj1 = Subject()
obj._name = "Chudamani"
# calling by object of student class
print(obj._name)
print(obj._funcName())

# Calling by object of Subject class
print(obj1._name)
print(obj1._funcName())