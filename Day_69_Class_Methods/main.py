# Python Class Method
# ? In python, classes are a way to define custom data types that can store data and define functions that can manipulate the data. One type of function that can be defined within a class is called a "method".
  # A class method is a type of method that is bound to the class and not the instance of the class. In other words, it operates on the class as a whole, rather than on a specific instance of the class. Class methods are defined using the "@classmethod" decorator, followed by a function definition. The first argument of the function is always 'cls', which represents the class itself.
# Class methods are useful in several situations. For example, we might want to create a factory method that creates instances of our class in a specific way. We could define a class method that creates the instances and returns it to the caller. Another common use case is to provide alternative constructors for our class. This can be useful if we want to create instances of our class in multiple ways, but still have a consistent interface for doing so.

# ? Example 
class ExampleClass:
  @classmethod
  def factory_method(cls, arg1, arg2):
    return cls(arg1, arg2)
  
class Employee:
  company = "Apple"
  def show(self):
    print(f"The name is {self.name} and company is {self.company}")
  @classmethod
  def changeCompany(cls, newCompany):
    cls.company = newCompany
e1 = Employee()
e1.name = "Chudamani"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)