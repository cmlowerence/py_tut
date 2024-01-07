# Hybrid and Hierarchical Inheritance
# ?Hybrid Inheritance
class BaseClass:
  pass

class Derived1(BaseClass):
  pass

class Derived2(BaseClass):
  pass

class Derived3(Derived1, Derived2):
  pass

class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def show_details(self):
    print(f"Name: {self.name}")
    print(f"Age: {self.age}")
    
class Person(Human):
  def __init__(self, name, age, address):
    Human.__init__(self, name, age)
    self.address = address
  
  def show_details(self):
    Human.show_details(self)
    print("Address: ", self.address)


class Program:
  def __init__(self, program_name, duration):
    self.program_name = program_name
    self.duration = duration
  def show_details(self):
    print("Program Name: ", self.program_name)
    print("Duration: ", self.duration)

class Student(Person):
  def __init__(self, name ,age, address, program):
    Person.__init__(self, name, age, address)
    self.program = program
  
  def show_details(self):
    Person.show_details(self)
    self.program.show_details()

program = Program("Computer Science", 4)
student = Student("John Doe", 25, '123 Main St.', program)
student.show_details()

# !Hierarchical Inheritance
class Animal:
  def __init__(self, name) -> None:
    self.name = name
  def show_details(self):
    print(f"Name: {self.name}")

class Dog(Animal):
  def __init__(self, name, breed) -> None:
    Animal.__init__(self, name)
    self.breed = breed
  def show_details(self):
    super().show_details()
    print(f"Species : Dog")
    print(f"Breed: {self.breed}")

class Cat(Animal):
  def __init__(self, name, color) -> None:
    super().__init__(name)
    self.color = color
  def show_details(self):
    super().show_details()
    print("Species: Cat")
    print(f"Color: {self.color}")
dog = Dog("Max", "Golden Retriever")
dog.show_details()
cat = Cat("Luna", "Black")
cat.show_details()

