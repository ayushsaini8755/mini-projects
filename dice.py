import random
roll = random.randint(1,6)
print("Hello!")
print("Please tell your name to create your username in this game")
name = input("Enter your name: ")
print("\n")
print("Your username in this game is:",name,"_5x_a")
print("WELCOME!",name,)
print("To the dice rolling game...........")
print("'Aim' of this game is to test your prediction power\n")
print("BASIC INSTRUCTIONS of this game are:")
print("1....You have only '5' or '3' chances according to the difficulty")
print("2....Predict a number which you get on the dice after rolling\n")
print("Is this good please comment 'Ok'")
inp = input("Enter here: ")
print("\n")
print("Please select the difficulty level of the game")
print("1.EASY")
print("2.HARD")
level = input("Enter your difficulty level: ")
print("\n")
if level=='1' or level=='Easy' or level=='EASY' or level=='easy':
  print("In this level you have '5' chances to predict the number")
  chances=5
  while chances>0:
    a = int(input("Enter your predicted number here: "))
    if a>=1 and a<=6:
      if roll==a:
        print("CONGRATULATIONS! you win this game in last",chances,"attempts")
        break
      else:
        chances-=1
        print("Wrong, Keep rolling the dice, but remember only",chances,"chances left\n")
      if chances==0:
        print("\nGAME OVER..........")
        print("BETTER LUCK TRY NEXT TIME.......")
        print("............................................")
    else:
        print("Please enter a valid number which present on the dice\n")
        
elif level=='2' or level=='Hard' or level=='HARD' or level=='hard':
  print("In this level you have only '3' chances to predict the number")
  chances=3
  while chances>0:
    a = int(input("Enter your predicted number here: "))
    if a>=1 and a<=6:
      if roll==a:
        print("CONGRATULATIONS! you win this game in last",chances,"attempts")
        break
      else:
        chances-=1
        print("Wrong, Keep rolling the dice, but remember only",chances,"chances left\n")
      if chances==0:
        print("\nGAME OVER..........")
        print("BETTER LUCK TRY NEXT TIME.......")
        print("............................................")
    else:
        print("Please enter a valid number which present on the dice\n")

else:
  print("Please select the valid difficulty level")
  print("Try Again.............")