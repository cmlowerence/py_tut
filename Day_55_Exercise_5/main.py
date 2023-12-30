# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the snake beats the water. Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.
import random
import time
snake = 0
water = 1
gun = 2
# options = {'snake': 0, 'water': 1, 'gun': 2}

"""
comp ->        S   W   G
player ->   S  0   1  -1

            W -1   0   1

            G  1  -1   0
"""




# ?      comp   player
# todo    |      |
# 0,0 = snake, snake #! Draw
# 0,1 = snake, water #! Loose
# 0,2 = snake, gun   #! Win
# 1,0 = water, snake #! Win
# 1,1 = water, water #! Draw
# 1,2 = water, gun   #! Loose
# 2,0 = gun, snake   #! Loose
# 2,1 = gun, water   #! Win
# 2,2 = gun, gun     #! Draw

def comp_choice(options = [['snake', 0],['water', 1],['gun', 2]]):
  return random.choice(options)


def check_win(comp_choice, player_choice):
  '''
  Parameter
  ---------
      >>> 0 for snake\n
      >>> 1 for water\n
      >>> 2 for gun\n
      ``input should be a int value of 0, 1 or 2. No other values are valid``
  '''
  # Loose set
  loose = {(0,1),(2,0),(1,2)}
  # Win set
  win = {(0,2),(1,0),(2,1)}
  if({(comp_choice,player_choice)}.issubset(win)):
    return 'Win'
  elif({(comp_choice,player_choice)}.issubset(loose)):
    return 'Loose'
  else:
    return 'Draw'

def handleUsrChoice(usr_input):
  if usr_input in ['snake','s']:
    return ['snake',0]
  elif usr_input in ['water', 'w']:
    return ['water', 1]
  elif usr_input in ['gun', 'g']:
    return ['gun', 2]
  else:
    return False

while True:
  usrInput = input('Press "Enter" to continue: ')
  if not usrInput == '':
    break
  print(" Lets us play game ".center(50,'='),end='\n\n')
  sets = int(input("How many rounds of game? : "))
  print("""Now this is a game where 3 choices are given:\n1) Snake\n2) Water\n3) Gun\nYou can enter any of these options and can even just enter first letter of these options (i.e. 's' for Snake, 'w' for Water and 'g' for Gun). Number input are not allowed""")
  print("Okay, Lets start!",end='\n\n')
  score = 0
  while sets > 0:
    comp = comp_choice()
    usr = input("Enter your choice: ").lower()
    if handleUsrChoice(usr):
      usr = handleUsrChoice(usr)
    else:
      print("Invalid Input. Please enter valid input option")
      continue
    result = check_win(comp_choice=comp[1],player_choice=usr[1])
    print(f"Your choice is '{usr[0].title()}' and computer's choice is '{comp[0].title()}'",end="\n\n")
    if result == 'Win':
      print('You win!😍')
      score += 100
    elif result == 'Loose':
      print("Oops! You loose 😟")
      score += 0
    else:
      print('This is a draw.😶')
      score += 0
    time.sleep(1)
    sets -= 1
    continue
