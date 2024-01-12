# Write a python program which reminds you of drinking water every hour or two. Your program can either beep or send desktop notifications for a specific operating system

import os
import subprocess
import time
from pync.TerminalNotifier import notify
import datetime

# ! Decorators
def signUp_decorator(fx):
  def wrapper():
    print()
    print("Sign Up Section".center(50,'-'))
    print()
    return fx()
  return wrapper

rootDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(rootDir)

tone_dir = './tones'

# # def countdown(timeout, function):
# #   time.sleep(timeout)
# #   function()

def say_print(msg):
  print(msg)
  subprocess.run(["say", msg])


# def water_reminder(timeout):
#   time.sleep(timeout)
#   msg = "It's time to drink water"
#   notifier(_title='Drink Water', _msg="Keep your body hydrated. Have a drink of water...", _sound=f"{tone_dir}/Glass.aiff", _appIcon="./icons/water-reminder.png")
#   say_print(msg)
#   print(f"Next drink after {round(timeout / 3600, 2)} hrs.")


# ===================================== Defining main function =====================================
def main():
  
  print("<------- Welcome again! Select the options below to proceed -------->")
  print()
  home_options = {
    "1" : {"text" : "Login", "function" : login_wrapper},
    "2" : {"text" : "SignUp", "function" : signUp_wrapper},
    "3" : {"text" : "Quit", "function" : exit_program},
  }
  
  for s_no in home_options:
    print(f"{s_no}. {home_options[s_no]['text']}")
    
  print()
  
  usr_input = input("Enter the option (S.No.): ")
  
  if usr_input in home_options:
    function_call = home_options[usr_input]['function']
    function_call()
  else:
    print("Wrong choice selected... Try Again ")
    print()
    main()

# ===================================== Greet Function =====================================
def greet():
  date_time = datetime.datetime.now().strftime("%d/%m/%YT%H:%M:%S").split("T")
  date = date_time[0]
  time_str = date_time[1]
  hrs = int(time_str.split(":")[0])
  greet = "Good Morning" if hrs < 12 else "Good Afternoon" if 12 <= hrs <= 16 else "Good Evening"
  say_print(greet)
  print(greet)
  return date

# ===================================== Function to exit the program =====================================
def exit_program():
  say_print("Bye! Have a great time...")
  exit()

# ===================================== Login Wrapper =====================================
def login_wrapper():
  print()
  print("Login Section".center(50,'-'))
  print()
  
  usr_name = input("Enter the username: ")
  password = input("Enter the password: ")
  usr_exist = verify_credentials(usr_name, password)
  
  if (not usr_exist):
    print()
    print("Logging in...")
    logged_in = login(usr_name, password)
    if (logged_in):
      login_body(usr_name, password)
  else:
    print("Username doesn't registered...")
    print(f"Select Options:\n\n1. Sign Up\n2. Exit\n3. Retry")
    choice = input("Enter the option: ")
    if (choice == "1"):
      print()
      print("Okay, Redirecting to SignUp section...")
      print()
      
      signUp_wrapper()
    elif (choice == "2"):
      print()
      print("Terminating Program...")
      exit_program()
    elif (choice == "3"):
      print()
      login_wrapper()
# ===================================== Login Function =====================================
def login(usr_name, password) -> bool:
  print("Login function called")
  return True

# ===================================== Login Body =====================================
def login_body(usr_name, password):
  login_options = {
        "1" : {"text" : "Start Water Reminder", "function" : water_reminder},
        "2" : {"text" : "Retrieve Data", "function" : retrieve_data},
        "3" : {"text" : "Back", "function" : login_wrapper},
        "4" : {"text" : "Quit", "function" : exit_program}
      }
  print()
  
  
  print("You will get 5 chances to choose correct option.")
  choice_count = 0
  
  while choice_count <= 5:
    for s_no in login_options:
      print(f"{s_no}. {login_options[s_no]['text']}")
    print()
    
    usr_choice = input("Enter the option (S.No.): ")
    
    if usr_choice in login_options:
      login_options[usr_choice]['function']()
    else:
      choice_count += 1
      if (choice_count == 5):
          print("Terminating Program")
          exit_program()
      else:
        print("Wrong option selected. Try Again!...")
        continue

# ===================================== Sign Up Wrapper =====================================
@signUp_decorator
def signUp_wrapper():
  usr_name = input("Enter the username: ")
  # If usr_name already exists, then ask for entering another username
  if usr_exist(usr_name):
    print("Username already exist. Choose any other username")
    signUp_wrapper()
  password = input("Enter the password: ")
  
  new_usr_status = handle_new_usr(usr_name, password)
  new_usr_status = "Success"
  if (new_usr_status == 'Success'):
    print("You have been successfully signed up...")
    print("Enjoy the services...")
    print()
    login(usr_name, password)
    login_body(usr_name, password)
  

# ===================================== Sign Up Function =====================================
def signUp() -> bool:
  print("SignUp function called")
  print()
  return True

# ===================================== Checking existing user =====================================
def usr_exist(usr_name) -> bool:
  return False

# ===================================== Verifying Credentials =====================================
def verify_credentials(usr_name, password):
  print("verify_credential function called")
  return True

# =============================== Create file_structure of the new user ===============================
def handle_new_usr(usr_name, password) -> str:
  print("Handling user...")
  
# ===================================== Retrieve Data =====================================
def retrieve_data():
  print("Retrieve Data function called...")
  pass

# Notification Function
def notification(**kwargs):
  app_icon = "./icons/water-reminder.png"
  tone = "./tones/Glass.aiff"
  notify(appIcon = app_icon, sound = tone, **kwargs)

# Water reminder function
def water_reminder():
  print("water_reminder function called")
  pass





if __name__ == "__main__":
  main()
  pass