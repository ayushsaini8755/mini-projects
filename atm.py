print("---------------------------")
print("           ATM            ")
print("---------------------------")
name = input("Please enter your name for atm verification: ")
print("VERIFIED")
print("Welcome '",name,"' to the ATM")
pin=3941
attempts=4
while attempts>0:
    entered_pin = int(input("Enter your atm pin: "))
    if entered_pin!=pin:
        attempts-=1
        print("INCORRECT PIN")
        print("\nOnly",attempts,"attempts left")
        print("Please try again......\n")
    else:
        print("Correct Pin\n")
        break
    if attempts==0:
        print("Card Blocked......\n")
if pin==entered_pin:
    print("Welcome to the Menu!")
    print("AVAILABLE CHOICES ARE:\n")
    print("1.VIEW BALANCE")
    print("2.WITHDRAW BALANCE")
    print("3.DEPOSIT BALANCE")
    print("4.Change Pin")
    print("5.EXIT")
    count=0
    while True:
      count+=1    
      choice = int(input("\nEnter your choice: "))
      if choice==1:
        print("Your current balance in your account is 1,00,000 ruppess")
      elif choice==2:
        amount = int(input("How much amount you want to withdraw: "))
        pin_1 = int(input("Please enter your account pin again for security purpose: "))
        if pin_1==pin:
          if 100000>=amount and amount>=100:
            current_ammount=100000-amount
            print("You withdraw",amount,"ruppess successfully")
            print("Current balance in your account is",current_ammount,"ruppess")
          else:
             print("Such low amount is not withdrawable")
             print("According to atm policy you withdraw atleast 100 ruppess")
        else:
          print("INCORRECT PIN")
          print("Failed to withdraw")
      elif choice==3:
        de_amount = int(input("How much amount you want to deposit in your account: "))
        total = de_amount+current_ammount
        print("Successfully deposited",de_amount,"ruppess in your account")
        print("Now your current balance in your account is",total,"ruppess")
      elif choice==4:
         print("You want to change your atm pin")
         pin_1 = int(input("Please enter your current atm pin: "))
         if pin_1==pin:
            print("OK!")
            a = int(input("Now enter your new atm pin: "))
            print("Your atm pin successfully changed")
            print("THANK YOU!\n")
         else:
            print("Your entered incorrect atm pin")
            print("Please enter correct atm pin again.......\n")
      elif choice==5:
         print("EXITED FROM ATM")
         print("THANK YOU FOR VISITING............\n")
         break
      else:
         print("INVALID CHOICE")
         print("ERROR OCCURING...........")
    



