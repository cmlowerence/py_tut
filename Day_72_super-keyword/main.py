# Super Keyword in Python
# ? The super() keyword in python is used to refer to the parent class. It is especially useful when a class inherits from multiple parent classes and we want to call a method from one of the parent classes.
# When a class inherits from a parent class, it can override or extend the methods defined in the parent class. However, sometimes we might want to use the parent class method in the child class. This where the super() keyword comes in handy

class ParentClass:
  def parent_method(self):
    print("This is the parent method")
class ChildClass(ParentClass):
  def child_method(self):
    print('This is the child method.')
    self.parent_method()
child_obj = ChildClass()
child_obj.child_method()

# The super() keyword is also useful when a class inherits from multiple parent classes. In this case, we can specify the parent class from which we want to call the method
# Example
# class A:
#   def show(self):
#     print("This is class A")
# class B:
#   def show(self):
#     print("This is class B")
# class C(A,B):
#   def show(self):
#     print("This is class C")
#     super(A,self).show()
#     super(B,self).show()
class A:
    def show(self):
        print("This is class A")

class B:
    def show(self):
        print("This is class B")

class C(A, B):
    def show(self):
        print("This is class C")
        super(A, self).show()  # Calls the show method of class A
        super(B, self).show()  # Calls the show method of class B

# Creating an instance of class C
c_obj = C()

# Calling the show method of class C
c_obj.show()


    
# c = C()
# c.show()