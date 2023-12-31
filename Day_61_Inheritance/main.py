# Inheritance in Python
# ?When a class derives from another class. The child class will inherit all the public and protected properties and methods from teh parent class. In addition, it can have its own properties and methods, this is called as inheritance.

# * Python Inheritance Syntax
class BaseClass:
  # Body of base class
  pass
class DerivedClass(BaseClass):
  # Body of derived class
  pass


# Q: Types of inheritance
'''
#*1) Single Inheritance
#*2) Multiple inheritance
#*3) Multilevel inheritance
#*4) Hierarchical Inheritance
#*5) Hybrid Inheritance

'''

# Q: Single Inheritance:
# ? Single inheritance enables a derived class to inherit properties from a single parent class, thus enabling reusability and the addition of new features to existing code
# Example
class Parent:
  def func1(self):
    print("This function is in parent class.")
class Child(Parent):
  def func2(self):
    print("This function is in child class.")
    
object = Child()
object.func1()
object.func2()


# Q: Multiple Inheritance:
# ? When a class can de derived from more than one base class, this type of inheritance is called multiple inheritances. In multiple inheritances, all the features of the base class are inherited into the derived class
# Example
class Mother:
  mother_name = "Kirna Devi"
  def mother(self):
    print(self.mother_name)
class Father:
  father_name = "Puran Chand"
  def father(self):
    print(self.father_name)
class Son(Mother, Father):
  def parents(self):
    print(f"Father name is : {self.father_name}")
    print(f"Mother name is : {self.mother_name}")
    
s1 = Son()
s1.parents()

# Q: Multilevel Inheritance
# ? In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. This is similar to a relationship representing a child and a grandfather
# Example
class GrandFather:
  def __init__(self,grand_father_name):
    self.grand_father_name = grand_father_name
class Father(GrandFather):
  def __init__(self, father_name, grand_father_name):
    self.father_name = father_name
    GrandFather.__init__(self,grand_father_name)
class Son(Father):
  def __init__(self, son_name, father_name, grand_father_name):
    self.son_name = son_name
    Father.__init__(self, father_name, grand_father_name)
    
  def print_name(self):
    print(f"Grandfather name: {self.grand_father_name}")
    print(f"Father name : {self.father_name}")
    print(f"Son name: {self.son_name}")
s1 = Son("Prince", "Rampal", "Lal Mani")
print(s1.grand_father_name)
s1.print_name()


# Q: Hierarchical Inheritance:
# ? When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance. In this program, we have a parent (base) class and two child(derived classes

# Example
class Parent:
  def func1(self):
    print("This is parent class function")
class Child1(Parent):
  def func2(self):
    print("This is child class function")
class Child2(Parent):
  def func3(self):
    print("This is Child 2 class function")


object1 = Child1()
obj2 = Child2()
obj2.func1()
object1.func2()



# Q: Hybrid Inheritance:
# Inheritance consisting of multiple types of inheritance.

# Example
class School:
  def func1(self):
    print(f"This function is in school.")
class Student1(School):
  def func2(self):
    print("This function is n student 1. ")
    
class Student2(School):
  def func3(self):
    print("This function is in student 2.")
    
class Student3 (Student1, School):
  def func4(self):
    print("This function is in student3")
object = Student3()
object.func1()
object.func2()