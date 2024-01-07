# The time Module in python
# ? The time module in python provides a set of function to work with time-related operations, such as timekeeping, formatting, and time conversions. This module is part of the Python Standard Library and is available in all Python installations, making it a convenient and essential tool for a wide range of applications. In this day 84 tutorial, we'll explore the time module in Python and see how it can be used in different scenarios

# * time.time()
# ? The time.time() function returns the current time as a floating-point number, representing the number of seconds since the epoch (the point in time when the time module was initialized). The returned value is based on the computer's system clock and is affected by time adjustments made by the operation system, such as daylight saving time. Here's an example

import time
print(time.time())


# * time.sleep()
# ? The time.sleep() function suspends the execution of the current thread for a specified number of seconds. This function can be used to pause the program for a certain period of time, allowing other parts of the program to run, or to synchronize the execution of multiple threads. Here is an example:

print("Start: ", time.time())
time.sleep(2) # seconds as argument
print("End: ", time.time())

# * time.strftime()
# ? The time.strftime() function formats a time value as a string, based on a specific format. This function is particularly useful for formatting dates and times in a human-readable format, such as for display in a GUI, a log file, or a report. Here is example:

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d  %H:%M:%S", t)
print(formatted_time)