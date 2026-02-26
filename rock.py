print("WELCOME! TO THE")
print("ROCK PAPER SCISSOR GAME\n")
print("Available Choices are:")
choices = ['rock', 'paper', 'scissor']
print(choices)
print("\n")
import random
while True:
   print("Select the difficulty level of the game")
   print("1......EASY")
   print("2......HARD")
   level = input("\nEnter your difficulty level: ")
   if level=='1' or level=='EASY' or level=='Easy' or level=='easy':
     print("In this level you '5' chances to play\n")
     print("Initial user score is 0")
     print("Initial computer score is 0\n")
     user_score = 0
     computer_score = 0
     chances=5
     while chances>0:
      comp = random.choice(choices)
      user = input("Enter your choice: ")
      chances-=1
      if user=='quit':
        print("Now you are exit from the game")
        break
      if user==comp:
       print("Tie!\n")
      elif user=='rock' and comp=='scissor':
       print("You Win!\n")
       user_score+=1
      elif user=='scissor' and comp=='paper':
        print("You Win!\n")
        user_score+=1
      elif user=='paper' and comp=='rock':
        print("You Win!\n")
        user_score+=1
      elif user not in choices:
        print("INVALID OPTION!.........\n")
        continue
      else:
        print("Computer Win!\n")
        computer_score+=1
    
     print("User Final Score is",user_score)
     print("Computer Final Score is",computer_score)
     if user_score > computer_score:
       print("\nFINALLY! User Win, this game.........")
       print("......................")
     elif computer_score > user_score:
       print("\nFINALLY! Computer Win, this game...........")
       print("BETTER LUCK TRY NEXT TIME.............")
       print("...............")
     else:
      print("Tie!....................\n")
   
     print("If you want to play again enter 'yes' or 'no'")
     again = input("\nEnter here: ").lower()
     print("\n")
     if again !='yes':
       print("Thanks For Playing.........")
       print("..................")
       break
    
   elif level=='2' or level=='HARD' or level=='Hard' or level=='hard':
     print("In this level you have only '3' chances to play\n")
     print("Initial user score is 0")
     print("Initial computer score is 0\n")
     user_score = 0
     computer_score = 0
     chances=3
     while chances>0:
      comp = random.choice(choices)
      user = input("Enter your choice: ")
      chances-=1
      if user=='quit':
        print("Now you are exit from the game")
        break
      if user==comp:
       print("Tie!\n")
      elif user=='rock' and comp=='scissor':
       print("You Win!\n")
       user_score+=1
      elif user=='scissor' and comp=='paper':
        print("You Win!\n")
        user_score+=1
      elif user=='paper' and comp=='rock':
        print("You Win!\n")
        user_score+=1
      elif user not in choices:
        print("INVALID OPTION!.........\n")
        continue
      else:
        print("Computer Win!\n")
        computer_score+=1
    
     print("User Final Score is",user_score)
     print("Computer Final Score is",computer_score)
     if user_score > computer_score:
       print("\nFINALLY! User Win, this game.........")
       print("......................")
     elif computer_score > user_score:
       print("\nFINALLY! Computer Win, this game...........")
       print("BETTER LUCK TRY NEXT TIME.............")
       print("...............")
     else:
      print("Tie!....................\n")
   
     print("If you want to play again enter 'yes' or 'no'")
     again = input("\nEnter here: ").lower()
     print("\n")
     if again !='yes':
       print("Thanks For Playing.........")
       print("..................")
       break
   else:
     print("\nSELECT A VALID DIFFICULTY LEVEL..............")
     print("............................\n")
     continue
     

