# Map, Filter and Reduce
# ? In python, the map, filter, and reduce functions are built-in functions that allow us to apply a function to a sequence of elements and return a new sequence. These functions are known as higher-order functions, as they take other functions as arguments.

# Q: map function
# * The map function applies a function to each element in a sequence and return a new sequence containing the transformed elements. The map function has following syntax:

# ! map(function, iterable)

# ? The function argument is a function that is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object
# Example

# List of numbers
numbers = [1,2,3,4,5]
# Double each number using the map functions
doubled = map(lambda x: x*2, numbers)

# Print the doubled numbers
print(list(doubled))


# Q: filter function

# * The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence containing only the elements that meats the predicate. The filter function has the following syntax:

# ! filter(predicate, iterable)
# ? The predicate argument is a function that returns a boolean value and is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.
# Example

# List of numbers
numbers = [1,2,3,4,5]

# Get only the even numbers using the filter function
evens = filter(lambda x : x % 2 == 0, numbers)

# Print the even numbers
print(list(evens))

# Q: reduce function
# * The reduce function is a higher-order function that applies a function to a sequence and returns a single value. It is a part of the functools module in python and has the following syntax:

# ! reduce(function, iterable)

# ? The function argument is a function that takes in two arguments and returns a single value. The iterable argument is a sequence of elements, such as a list or tuple.
# * The reduce function applies the function of the first two elements in the iterable and then applies the function to the result and the next element, and so on. The reduce function returns the final result.

# Example
from functools import reduce
# A number list
numbers = [1,2,3,4,5,6,7,8,9,10]
sum_num = reduce(lambda x, y: x + y, numbers)
print(sum_num)