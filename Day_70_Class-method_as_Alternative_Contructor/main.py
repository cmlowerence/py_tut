# Class methods as alternative constructors

# ? In OOP, the term "constructor" refers to a special type of method that is automatically executed when an object is created from a class. The purpose of a constructor is to initialize the object's attributes, allowing the object to be fully functional and ready to use
# * A class method belongs to the class rather than to an instance of the class One common use case of class method as alternative constructor is when we want to create an object from data that is stored in different format, such as string or dictionary. For example consider a class named "Person" that has two attributes: "name" and "age". The default constructor for the class might look like:
class Person: 
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
# But what if we want to create a Person object from a string that contains the person's name and age separated by a comma? We can define a class method named "from_string" to do this

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  @classmethod
  def from_string(cls, string):
    name, age = string.split(',')
    return cls(name, int(age))
# Now we can create a Person object from a string like:
person = Person.from_string("John Doe, 30")
print(person.name)
print(person.age)

# Another common use case for class methods as alternative constructors is when we want to create an object with a different set of default values than what is provided by the default constructor. For example, consider a class named "Rectangle" the has two attributes: "width" and "height". The default constructor for the class might look like this:

class Rectangle:
  def __init__(self, width: type[int], height : type[int]):
    self.width = width
    self.height = height
# ? But what if we want to create a Rectangle object with a default width of 10 and default height of 5? We can define a class method named "square" to do so:
class Rectangle:
  def __init__(self, width: type[int], height : type[int]):
    self.width = width
    self.height = height
  @classmethod
  def square(cls, size:type[int]):
    return cls(size, size)
  
# now we can create a square rectangle like:
rectangle = Rectangle.square(10)