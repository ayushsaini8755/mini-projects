print("WELCOME!\nAyush")
print("To the number guessing game")
print("Please select the difficulty level of the game")
print("1.EASY")
print("2.MEDIUM")
print("3.HARD")
level = input("Enter the difficulty level: ")
import random
num = random.randint(180,200)
if level=='1' or level=='EASY' or level=='easy' or level=='Easy':
 print("In this level you have unlimited chances and unlimited hints for guessing a number")
 attempts=0
 while True:
        guess = int(input("Enter your guess: "))
        attempts+=1
        if guess>=300:
             print("Your guess is too big")
        elif guess<100:
             print("Your guess is too small")
        elif guess>=100 and guess<170:
             print("Your guess is low small")
        elif guess>=170 and guess<200:
            print("Your guess is just close")
        elif guess>200 and guess<=230:
            print("Your guess is just close")
        elif guess>230 and guess<=270:
             print("Your guess is low big")
        elif guess>270 and guess<300:
             print("Your guess is big")
        else:
             print("Correct! You guessed it in",attempts,"attempts")
             break
elif level=='2' or level=='medium' or level=='Medium' or level=='MEDIUM':
     print("In this level you have only five attempts and hints are given for guessing the number")
     attempt=5
     while attempt>0:
           Guess=int(input("Enter your guess: "))
           if Guess==200:
               print("\nYour guess it right")
               print("CONGRATULATIONS! you win this game")
               break
           else:
            attempt-=1
            if Guess>300:
                print("Your guess is too big")
            if Guess>250 and Guess<=300:
                print("Your guess is big")
            if Guess<100:
                print("Your guess is too small")
            if Guess>=100 and Guess<150:
                print("Your guess is small")
            if Guess>=150 and Guess<200:
                print("Your guess is just close")
            if Guess>200 and Guess<=250:
                print("Your guess is just close")
            if attempt==0:
                print("\nYou Lose")
                print("\nGAME OVER..............") 
                print(".............")
                print(".......")
        
elif level=='3' or level=='HARD' or level=='hard' or level=='Hard': 
     print("In this level you have only five attempts, but no hints are given for guessing the number")
     attempt=5
     while attempt>0:
          Guess=int(input("Enter your guess: "))
          if Guess==200:
               print("\nYour guess it right")
               print("CONGRATULATIONS! you win this game")
               break
          else:
               attempt-=1
               print("Wrong Guess")
          if attempt==0:
               print("\nYou Lose")
               print("\nGAME OVER................")
               print(".............")
               print(".......")
else:
    print("\nInvalid Difficulty Level")
    print("Try Again")
    print("ERROR OCCURING..................")

