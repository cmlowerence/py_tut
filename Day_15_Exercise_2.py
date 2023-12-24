# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour.

import time
dayHr = int(time.strftime("%H"))
if (dayHr>=0 and dayHr<12):
  print("Good Morning")
elif(dayHr>=12 and dayHr<5):
  print("Good Afternoon")
else:
  print("Good Evening")
