from module import Magic
# Magic/Dunder Methods in Python
# ? These are special methods that we can define in our classes, and when invoked, they give you a powerful way to manipulate objects and their behavior.

# Magic methods, also known as 'dunder' from the double underscores surrounding their names, are powerful tools that allows us to customize the behavior of our classes. They are used to implement special methods such as the addition, subtraction and comparison operators, as well as some more advanced techniques like descriptors and properties.


# * __init__ method
# ? The __init__ method is a special method that is automatically invoked when we create a new instance of a class. This method is responsible for setting up the object's initial state, and it is where we would typically define any instance variables that we need.
obj1 = Magic()
print(obj1.author)
obj1.roll = 23

# __str__ and __repr__ method
# ? THe str and repr methods used to convert an objet to a string representation. The str method is used when we want to print out an object, while the repr method is used when we wnt to get a string representation of an object that can be used to recreate the object

obj2 = Magic()
print(str(obj2))
print(repr(obj2))


# __len__ method
# ? The len method is used to get the length of an object. This is useful when you want to be able to find the size of a data structure, such as a list or dictionary.
# Example
class MyList():
  def __init__(self, list = []):
    self.list = list
  def __len__(self): # This method will return the count of the elements in the list and return the content for len function
    len = 0
    for item in self.list:
      len += 1
    return len
obj3 = MyList([1,2,3,4,5])
print(len(obj3))

# __call__ method
# ? The call method is used to make an object callable, meaning that we can pass it as a parameter to a function and it will be executed when the function is called. This is an incredibly powerful tool that allows us to create objects that behave like function.

obj4 = Magic()
print(obj4())