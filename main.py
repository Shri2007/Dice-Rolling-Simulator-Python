import random
min = 1
max = 6
roll_again = "yes"

while roll_again == "yes" or roll_again == "Yes" or roll_again == "y":
  print("Rolling the dice...")
  print("The numbers are")
  print(random.randint(min, max))
  print(random.randint(min, max))
  
  roll_again = input("Want to roll again? ")
  hi = "no"
if hi == "no":
  print("Ok!")
  print("Bye!")
else:
 print("Ok!")

