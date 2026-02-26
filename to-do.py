print("\n-----------------------------------------")
print("       WELCOME TO THE TO-DO LIST")
print("-----------------------------------------")
print("\nHere you can add your daily tasks and when completed you can delete as well........")
print("...................................................................................\n")
ac = input("")
while True:
   print("-------------------")
   print("SELECT YOUR CHOICE")
   print("-------------------")
   print("1.Add task")
   print("2.View task")
   print("3.Delete all tasks")
   print("4.Exit\n")
   choice = input("Enter your choice: ")
   if choice=='1':
     no = int(input("\nEnter how many task you want to add: "))
     print("So, you want to add",no,"tasks......")
     print("\n")
     count=no
     while count>0:
         task = input("Enter your tasks here: ")  
         with open("sample.txt","a+") as file:
            file.write(task + "\n")
            count-=1
     print("\nYour all",no,"tasks are added successfully...........")
   elif choice=='2':
      with open("sample.txt","r") as file:
         data = file.read()
         print("Your saved tasks are here\n")
         print(data)
   elif choice=='3':
       with open("sample.txt","w") as file:
          file.write("-----------------------\n")
          file.write(".......................\n")
          print("\nYour all saved tasks are deleted successfully")
   elif choice=='4':
      print("Thanks for using...........")
      print("...............................")
      break
   else:
      print("\nINVALID CHOICE.........")
      print("RE-ENTER YOUR CHOICE AGAIN...............\n")
      continue
   print("\n-----------------------")
   print("If you want to use again") 
   a = input("Enter 'yes' or 'no' here: ")
   print("-----------------------\n")
   if a!='yes':
        print("\nThanks for using.................")
        print(".............................")
        break

    
      

        




