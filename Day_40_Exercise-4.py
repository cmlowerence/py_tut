import random
import string
# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret language

# Coding:
# ?> if the word contains at-least 3 characters: 
#  ?>Remove the first letter and append it at the end
# ?> now append three random characters at the starting and the end
# else:
# ? simply reverse the string

# decoding
# if the word contains less than 3 characters:
# ? reverse it
# else:
# ? remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask weather you want to coe or decode

def random_char(char_count):
  return ''.join(random.choices(string.ascii_letters,k=char_count))

# !Function that encodes
def encode(word):
  if len(word) >= 3:
    return random_char(3) + word[1:] + word[0] + random_char(3)
  else:
    return word[::-1]

# !Function that decodes
def decode(encode):
  if len(encode) < 3:
    return encode[::-1]
  else:
    decode = encode[3:-3]
    return decode[-1] + decode[:-1]
class OptionError(Exception):
  def __init__(self,value):
    self.value = value
    self.message = f"Invalid input: {value}. Please provide '1' or '2' only."
    super().__init__(self.message)
class InvalidCodeToDecode(Exception):
  def __init__(self, value):
    self.value = value
    self.message = f"This is not a coded message: {value}. Coded message should be either of 2 word or 9 and above words"
    super().__init__(self.message)
while True:
  try:
    # Taking Input
    codeOrDecode = input("What do you want to do(1 for code and 2 for decode): ")
    # !Checking valid input
    if (codeOrDecode not in ('1', '2')):
      raise OptionError(codeOrDecode)
    
    # ? Coding and Decoding
    if (codeOrDecode == '1'):
      # Q: coding
      word = input("Enter the word you want to code: ")
      print(encode(word))
      break
    else:
      # Q: decoding
      word = input("Enter the word you want to decode: ")
      if 2 < len(word) < 9:
        raise InvalidCodeToDecode(word)
      print(decode(word))
      break
  except OptionError or InvalidCodeToDecode as e:
    print(e.message)
    continue
  
