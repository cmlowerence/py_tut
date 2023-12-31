# Getters
# Getters in Python are methods that are used to access the values of an object's properties. They are used to return the value of a specific property, and are typically defined using the @property decorator. Here is an example of a example of a simple class with a getter method:

class MyClass:
  def __init__(self, value):
    self._value = value
  @property
  def get_value(self):
    return self._value
# ? In this example, the MyClass class has a single property, _calue, wich is initialized in the __init__ method. The value method is defined as a getter using the @property decorator, and is used to return the value of the _value property
# * To use the getter, we can create an instance of the MyClass class, and then access the value property as if it were an attribute
# Example
obj = MyClass(10)
print(obj.get_value)

# Q: Setters
# ? It is important to note that the getters do not take any parameters and we can't set the value through getter method. For that we need setter method which can be added by decorating method with @property_name.setter

# Example
class MyClass1:
  def __init__(self,value):
    self._value = value
  @property
  def value(self):
    return self._value
  @value.setter
  def value(self, new_value):
    self._value = new_value

# Use
obj1 = MyClass1(40)
print(obj1.value)
obj1.value = 100
print(obj1.value)