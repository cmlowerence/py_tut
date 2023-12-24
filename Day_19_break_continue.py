# break statement
for i in range(1,101,1):
  print(i,end=" ")
  if (i==50):
    break
  else:
    print("Mississippi")
print("That's all")

# continue statement
# this statement skips the rest of the loop statement and cause the next iteration to occur
for i in [2,3,4,6,8,0]:
  if (i%2!=0): #! skips the number which is not divisible by 2
    continue
  print(i)