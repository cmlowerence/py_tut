# Method overriding in python
# ? Method overriding is a powerful feature in object-oriented programming that allows us to redefine a method in a derived class. The method in the derived class is said to override the method in the base class. When we create an instance of the derived class and call the overridden method, the version of the method is derived class is executed, rather than the version in the base class.
# * In Python, method overriding is a way to customize the behavior of a class based on its specific needs.
# Example:
class Shape:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  @property
  def area(self):
    return self.x * self.y
# In the base class, the area method is defined, but does not have any implementation. If we want to create a derived class that represents a circle, we can override the area method and provide an implementation that calculates the area of a circle

class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius
  @property
  def area(self):
    return 3.14 * (self.radius ** 2)
  
rec = Shape(3,5)
print(rec.area)

c = Circle(4)
print(c.area)