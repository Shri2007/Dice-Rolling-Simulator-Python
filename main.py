import random
#This is telling the code this is a randomizer.
min = 1
#The minimum of a dice is 1.
max = 6
#The maximum of a dice is 6.
roll_again = "yes"
#Variables can also be a string.
while roll_again == "yes" or roll_again == "Yes" or roll_again == "y" or roll_again == "Y":
  #The while loop which will loop over and over again.
  print("Rolling the dice...")
  print("The numbers are")
  print(random.randint(min, max))
  print(random.randint(min, max))
  #This gives a random number
  
  roll_again = input("Want to roll again? ")
  #If you say "Yes", this will continue.
