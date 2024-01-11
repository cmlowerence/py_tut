# Function caching 
# Function caching is a technique of improving the performance of a program by storing the result of a function call so that we can reuse the results instead of recomputing them every time the function is called.

from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
  time.sleep(5)
  return n*5

print(fx(20))
print("Done of 20")

print(fx(2))
print("Done for 2")

print(fx(6))
print("Done for 6")


print(fx(20))
print("Done of 20")

print(fx(2))
print("Done for 2")

print(fx(6))
print("Done for 6")

