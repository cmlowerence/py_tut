# How importing in python works
# ? Importing in python is the process of loading code from a python module into the current script. This allows us to use the functions and variables defined in the module in our current script, as well as any additional modules that the imported module may depend on.
# * To import a module in python, we use the import statement followed by the name of the module. For example, to import math module, which contains variety of mathematical functions, we would use the following statement:

import math

# ? Once a module is imported, we can use any of the function and variables defined in the module by using the dot notation like:

result = math.sqrt(9)
print(result) # 3.0

# we can also import multiple functions and variables at once by separating them with a comma:
from math import sqrt, pi
print(sqrt(9))
print(pi)

# It's also possible to import all functions and variables from a module using the * wildcard. However, this is generally not recommended as it can lead to confusion and make it harder to understand where specific functions and variables are coming from.
from math import *
print(sqrt(25))
print(pi)
print(sin(90))

# Python also allows us to rename imported modules using the as keyword. This can be useful if we want to use a shorter or more descriptive name for a module or if we want to avoid naming conflicts with other modules or variables in our code
# Q: The 'as' keyword
import math as m
print(m.pi)

# Q: The dir() function
# ? Python has a built-in function called dir that we can use to view the names of all the functions and variables defined in a module. This can be helpful for exploring and understanding the contents of a new module.
import math
print(dir(math)) # This will output a list of all the names defined in the math module, including function like sqrt and pi, as wll as other variables and constants.


# custom modules
# ? We can create custom modules defined by us. We can do it by just creating a file in the same directory or in the directory where other modules are stored.
# * For Example I have created a module name module.py in the same directory and I can import it as a module as
import module # ! Custom module
print(module.name) # ! Chudamani
print(module.sum(45,34)) # ! 79