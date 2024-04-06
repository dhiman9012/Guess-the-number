import random 
target=random.randint(1,100)

while True:
  userChoice=int(input("Guess the target or Quit press 0:"))
  if(userChoice==0):
    break

  if(userChoice==target):
    print("Sucess: Correct Guess!!")
    break

  elif(userChoice<target):
    print("Your number is too small .Take big number......")
  else:
    print("Your number is too big .Take small number.....")




##print("--------------Game Over---------------")