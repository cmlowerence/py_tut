from datetime import date as calender
class Magic():
  def __init__(self, author = "Chudamani", date = calender.today().strftime("%d/%m/%Y")):
    self.author = author
    self.date = date
  def __str__(self):
    return f"This is an Magic object written by {self.author} on {self.date}"
  def __repr__(self):
    return f"This is repr() function of the object written by {self.author} on {self.date}"
  def __len__(self):
    '''
    Characters in author's name
    ---------------------------
    The len function in this class will return the number of characters in the name of the author
    '''
    i = 0
    for j in self.author:
      i += 1
    return i
  def __call__(self):
    return {'author' : self.author, 'date': self.date}