# Function arguments and return statements

# Four types of arguments
# > Default Arguments
# > Keyword arguments
# > Variable length arguments
# > Required Arguments
# ? Default Arguments
def name(fname,mname="Felix Anthony", lname = "Cena"):
  print("Hello", fname,mname,lname)
name("John")

# ? Keyword arguments
# We can pass arguments as key = value pair while calling the function. Doing this, order of argument doesn't matters
name(fname="Chudamani",lname="Stark",mname="Lawrence") # !not in order but still works

# ? Required Arguments
# we must give the argument to the function which are essential for it (i.e. if argument are not assigned default value). If we don't, error will occur

# ? Variable length arguments
# sometimes we may nee to pass more arguments than those define in teh actual function. Tis ca=n be done using variable-length arguments.
# There are two ways to achieve this
# *> Arbitrary arguments:
def name1(*name):
  print("Hello, ", name[0],name[1],name[2])
name1("Chudamani","Rishi","Virender")

# *> Keyword Arbitrary Arguments:
def name2(**name):
  print("Hello,",name["fname"],name["mname"],name["lname"])
  # here fname, mname and lname are keys 
name2(fname = "Chudamani",lname="Lawrence",mname="James")


# ? Return statement
# the return statement is used to return the value of the expression back to the calling function

def name3(fname,mname,lname):
  return f"Hello, {fname} {mname} {lname}"
print(name3("Chudamani","Hero","Lawrence"))