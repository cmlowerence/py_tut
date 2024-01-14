# Multithreading in python

# ? Multithreading is a technique in programming that allows multiple threads of execution to run concurrently within a single process. In Python, we can use the threading module to implement multithreading.

import threading
import time
from concurrent.futures import ThreadPoolExecutor
# creating a thread
# ? To create a thread, we need to create a Thread object and then call its start() method. The start() method runs teh thread and then to stop the execution, we need the join() method.
# Example

def func(seconds):
  print(f"Sleeping for {seconds} seconds.")
  time.sleep(seconds)
  print(f"Function awake after {seconds} seconds")
  return seconds

# def poolingDemo():
#   with ThreadPoolExecutor() as executer:
#     future1 = executer.submit(func, 3)
#     future2 = executer.submit(func, 2)
#     future3 = executer.submit(func, 4)
#     print(future1.result())
#     print(future2.result())
#     print(future3.result())
  
# Threading with map function 
def poolingDemo():
  with ThreadPoolExecutor() as executer:
    l = [3,5,1,2] #! Our arguments for the functions
    results = executer.map(func, l)
    for result in results:
      print(result)
    # return results
    
poolingDemo()
print("Program terminated...")

# start_time = time.perf_counter()
# start_time = time.perf_counter()

# # Normal Code
# # func(2)
# # func(1)
# # func(5)
# # func(4)

# # Some code with thread
# t1 = threading.Thread(target=func, args=[2])
# t2 = threading.Thread(target=func, args=[4])
# t3 = threading.Thread(target=func, args=[1])

# # Starting threads
# t1.start()
# t2.start()
# t3.start()

# # Awaiting the functions to be done
# t1.join()
# t2.join()
# t3.join()

# end_time = time.perf_counter()
# print(f"Total time taken: {end_time - start_time}")