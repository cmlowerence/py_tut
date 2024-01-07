import os
def say(sentence):
  os.system(f"say {sentence}")

user_list = ["Chudamani", "Yuvraj", "Rishi", "Virender", "Chopender", "Bhoju", "Rakesh", "Ajay", "Akshay"]
for name in user_list:
  print(f"Shout_out to {name}")
  say(f"Shout_out to {name}")