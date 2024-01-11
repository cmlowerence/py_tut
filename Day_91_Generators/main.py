# Generators in python
# ? Generators in python are special type of functions that allow us to create an iterable sequence of values. A generator function returns a generator object, which can be used to generate the values one-by-one as you iterate over it. Generators are powerful tool for working with large or complex data sets, as they allow you to generate the values on the fly, rather than having to create and store teh entire sequence in memory

# Creating a generator

def my_generator():
  for i in range(5):
    yield i
    
gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
print(next(gen))


for j in gen:
  print("for loop")
  print(j)