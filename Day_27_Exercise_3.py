from random import random
import time
# Create a program capable of displaying questions to the user like KBC. Use the list datatype to store teh questions and their correct answers. Display the final amount the person is taking home after playing the game.

print(' KBC '.center(40,'-'))
questionBank = [["What is capital of india?","New Delhi"],["Which country reach in Mars orbit in their first attempt?","India"],["Which place in himachal is known as 'Alora of Himachal'?","Masroor Rock Temple"],["Ideal temperature (in Kelvin) require for Superconductivity of a material is: ","0"],["NCF was established in which year?","2005"]]

# Functions
def fetchQuestion(questionBank):
  qst = questionBank[round(random()*(len(questionBank)-1))]
  questionBank.pop(questionBank.index(qst))
  return qst

def correctAns(qst,usrAns):
  if qst[1].lower() == usrAns.lower():
    return True
  else:
    return False


questionCounter = 1
winning = 0
while (questionCounter <=5):
  qst = fetchQuestion(questionBank)
  usrAns = input(f"{qst[0]}\n")
  if correctAns(qst,usrAns):
    if (winning == 0):
      winning = 7_000
    else:
      winning += questionCounter * winning
    questionCounter += 1
    time.sleep(.3)
    print(f"Correct Answer! You won {winning} money in total")
    time.sleep(1)
  else:
    print("Sorry, Wrong answer. Your winning are $",winning)
    break
