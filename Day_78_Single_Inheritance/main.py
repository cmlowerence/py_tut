# Single Inheritance
class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species
  def make_sound(self):
    print("Sound made by the animal")
class Dog(Animal):
  def __init__(self, name, breed):
    Animal.__init__(self, name, species='Dog')
    self.breed = breed
  def make_sound(self):
    print("Bark!")
    
# Quick quiz
# Implement a Cat class by using the animal class. Add some methods specific to cat
class Cat(Animal):
  def __init__(self, name, breed):
    self.name = name
    Animal.__init__(self, name, species='Cat')
    self.breed = breed
  def make_sound(self):
    print("Meow!")
  def abilities(self):
    abilities = ['quick response', 'fine reflexes', 'sharp teeth', 'cute', 'ferocious']
    for ability in abilities:
      print(ability.title())
cat = Cat('Kitty', 'American')
print(cat.name)
cat.make_sound()
cat.abilities()