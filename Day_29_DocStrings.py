# Docstring in python
# ? Python doc_strings are the string literals that appear right after the definition of a function, method, class, or module

# Example
def square(n):
  '''Takes a number and returns the square of that number'''
  print(n**2)
square(2)

# Example 2
def add(num1, num2):
  """
  Add up two integer numbers.
  This function simply wraps the ``+`` operator, and does not
  do anything interesting, except for illustrating what the docstring fo a very simple function look like.
  
  Parameters
  ----------
  num1 : int
      First number to add.
  num2 : int
      Second number to add.
      
  Returns
  -------
  int
    The sum of ``num1`` and ``num2``.
    
  See Also
  --------
  subtract : Subtract one integer from another
  
  Examples
  --------
  >>> add(2,2)
  4
  >>> add(25,0)
  25
  >>> add(10, -10)
  0
  """
  return num1 + num2
print(add())