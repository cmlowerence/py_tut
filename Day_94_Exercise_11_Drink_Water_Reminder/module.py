# Write a python program which reminds you of drinking water every hour or two. Your program can either beep or send desktop notifications for a specific operating system

import os
import subprocess
import time
import json
import re
from pync.TerminalNotifier import notify
import datetime

#  Decorators
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

# ================================== Function to speak =====================================
def say_print(msg):
  print(msg)
  subprocess.run(["say", msg])

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
    say_print("Wrong choice selected... Try Again ")
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
  subprocess.run(['say','Bye! Have a great time...'])
  print("Bye! Have a great time",end="",flush=True)
  time.sleep(.7)
  print(".",end="",flush=True)
  time.sleep(.7)
  print(".",end="",flush=True)
  time.sleep(.7)
  print(".",end="",flush=True)
  time.sleep(.7)
  exit()

# ===================================== Login Wrapper =====================================
def login_wrapper():
  print()
  print("Login Section".center(50,'-'))
  print()
  
  usr_name = input("Enter the username: ")
  password = input("Enter the password: ")
  usr_exist = verify_credentials(usr_name, password)
  
  if usr_exist:
    print()
    print("Logging in...")
    login(usr_name, password)
    login_body(usr_name, password)
  else:
    print()
    say_print("Username doesn't registered...")
    print(f"Select Options:\n\n1. Sign Up\n2. Exit\n3. Retry")
    choice = input("Enter the option: ")
    if (choice == "1"):
      print()
      say_print("Okay, Redirecting to SignUp section...")
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
def login(usr_name, password):
  global __user_name__, __password__
  __user_name__ = usr_name
  __password__ = password

# ===================================== Login Body =====================================
def login_body(usr_name, password):
  login_options = {
        "1" : {"text" : "Start Water Reminder", "function" : water_reminder},
        "2" : {"text" : "Retrieve Data", "function" : retrieve_data_display},
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
        print()
        exit_program()
      else:
        say_print("Wrong option selected. Try Again!...")
        continue

# ===================================== Sign Up Wrapper =====================================
@signUp_decorator
def signUp_wrapper():
  name = input("Enter your name: ")
  usr_name = input("Enter the username: ")
  # If usr_name already exists, then ask for entering another username
  if usr_exist(usr_name):
    say_print("Username already exist. Choose any other username")
    signUp_wrapper()
  password = input("Enter the password: ")
  
  new_usr_status = handle_new_usr(usr_name=usr_name, password=password,name=name)
  if (new_usr_status == 'Success'):
    print()
    say_print("You have been successfully signed up...")
    say_print("Enjoy the services...")
    print()
    login(usr_name, password)
    login_body(usr_name, password)

# ===================================== Checking existing user =====================================
def usr_exist(usr_name=None) -> bool:
  with open("./usr_data/data.json", 'r') as f:
    data = json.loads(f.read())
    usr_names = [srNo['usr_name'] for srNo in data.values()]
    
    if usr_name in usr_names:
      return True
    else:
      return False

# ===================================== Verifying Credentials =====================================
def verify_credentials(usr_name=None, password=None):
  try:
    with open("./usr_data/data.json", 'r') as f:
      data = json.loads(f.read())
      
      for usr_id, usr_data in data.items():
        if 'usr_name' in usr_data and 'password' in usr_data:
          if usr_data['usr_name'] == usr_name and usr_data['password'] == password:
            return True
      return False
  except FileNotFoundError:
    say_print("The user_data file not found. Terminating Program...")
    exit()
  except:
    say_print("Error in the process...")

# =============================== Create file_structure of the new user ===============================
def handle_new_usr(usr_name, password, name) -> str:
  if (usr_name is not None and password is not None):
    try:
      new_data = {}
      with open("./usr_data/data.json", "r") as f:
        data = json.load(f)
        id_list = list(data.keys())
        _id = int(id_list[-1]) + 1
        usr_dict = {f"{_id}" : {
          "usr_name" : usr_name,
          "password" : password,
          "name" : name,
          "activity_log" : [],
          "reminder_log" : []
        }}
        new_data = {**data,**usr_dict}
      with open("./usr_data/data.json", 'w') as f:
        f.write(json.dumps(new_data))
        return "Success"
    except FileNotFoundError:
      print("File not found.")
    except json.JSONDecodeError as e:
      print(f"Error decoding JSON: {e}")
  return "Failure"

  
# ===================================== Retrieve Data =====================================
def retrieve_data():
  try:
    global __user_name__
    if __user_name__:
      with open('./usr_data/data.json', 'r') as f:
        data = json.load(f)
        for _id, _data in data.items():
          if 'usr_name' in _data:
            if _data['usr_name'] == __user_name__:
              return _data.get("reminder_log", None)
    return None
  except:
    return None

def retrieve_data_display():
  data = retrieve_data()
  print()
  if data is not None:
    if not len(data) == 0:
      say_print("Here is your data...")
      print()
      for task in data:
        print(f"Time : {task['time']}\nData : {task['date']}\nDetail : {task['msg']}")
        print()
    else:
      say_print("No data of user is yet logged...")
  else:
    say_print("Error encounter. No Usr_data found!")
    return
# ===================================== Notification Function =====================================
def notification(**kwargs):
  app_icon = "./icons/water-reminder.png"
  tone = "./tones/Glass.aiff"
  notify(appIcon = app_icon, sound = tone,**kwargs)

# ===================================== Logging the details =======================================
def log_reminder():
  global __user_name__, __password__
  if (__user_name__ and __password__):
    with open('./usr_data/data.json', 'r+') as f:
      data = json.load(f)

      for user_id, user_data in data.items():
        if 'usr_name' in user_data and 'password' in user_data:
          if user_data['usr_name'] == __user_name__ and user_data['password'] == __password__:
            date_time = datetime.datetime.now().strftime("%d/%m/%YT%H:%M:%S").split("T")
            _date = date_time[0]
            _time = date_time[1]
            _msg = "Water Drank"
            log_data = {"time": _time, "date": _date, "msg": _msg}

            if "reminder_log" in user_data:
              user_data['reminder_log'].append(log_data)
            else:
              user_data['reminder_log'] = [log_data]

            # Move file cursor to the beginning and write the modified data
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()
            say_print("Data logged...")
          else:
            continue
  else:
    say_print("Error in logging")
    return None
  
  
  
# ===================================== Water reminder function =====================================
def water_reminder():
  print()
  print("Units can only be 'hr', 'min', and 'sec' only...")
  interval = input("Enter the time interval of notification(e.g. 10sec, 30min, 1hr, 2hr, 45min etc.): ")
  try:
    _interval_dict = Extract_Time(interval)
    interval_in_seconds = _interval_dict.in_seconds
    notification(message=f"Your Water reminder is up now. It will remind you to drink water every {interval}", title="Water Reminder", subtitle="...Be hydrated...")
    start_reminder(interval_in_seconds)
  except Exception as e:
    print(e)
    return


# ================================== Starting Reminder Function ===================================
def start_reminder(interval):
  try:
    while True:
      time.sleep(interval)
      notification(message="It's time to drink water buddy", title="Water Reminder")
      log_reminder()
      confirm = input("Hit enter to continue, type 'exit' to stop 'back' to go back: ")
      if confirm.lower() == 'exit':
        exit_program()
      elif confirm.lower() == 'back':
        return
  except KeyboardInterrupt:
      say_print("\nReminder stopped by user.")
      exit_program()


# Extracting time from string
class Extract_Time:
  SECONDS_PER_MINUTE = 60
  SECONDS_PER_HOUR = 3600
  
  def __init__(self,string) -> None:
    self.hour, self.minute, self.seconds = self.extract_time(string)
  
  def extract_time(self, string):
    # If the input is just the integer value with no units
    if string.isdigit():
      return 0, 0, int(string)
    
    pattern = r'(\d+)\s?(hr|min|sec)'
    matches = re.findall(pattern, string)
    _dict = {unit : int(number) for number, unit in matches}
    
    # Set default value if unit is missing
    return _dict.get('hr', 0), _dict.get('min', 0), _dict.get('sec', 0)
  
  @property
  def in_seconds(self):
    return (self.hour * self.SECONDS_PER_HOUR) + (self.minute * self.SECONDS_PER_MINUTE) + self.seconds

  @property
  def in_minutes(self):
    return (self.hour * self.SECONDS_PER_HOUR / self.SECONDS_PER_MINUTE) + (self.minute) + (self.seconds / self.SECONDS_PER_MINUTE)

  @property
  def in_hours(self):
    return (self.hour) + (self.minute / self.SECONDS_PER_MINUTE / self.SECONDS_PER_HOUR) + (self.seconds / self.SECONDS_PER_HOUR)

if __name__ == "__main__":
  main()
