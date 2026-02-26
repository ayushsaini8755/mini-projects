import random
import string
print("\n Welcome to the password strength cheaker")
a = input("Enter your password here:")
if len(a) >= 8 and any(char in string.punctuation for char in a):
   print("Strong Password")
else:
   print("Your Password is weak")

name = input("\n Enter your name = ")
print("Welcome",name,"to the Password Generator!")

pass_len = int(input("Please enter your password length = "))
if pass_len <= 7:
   print("If you want a secure password please enter length atleast of 8")
   pass_len = int(input("\n Please enter your password length again = "))
y = input("If you want to include your name characters in your password, type 'yes' else type 'no'\n")

password = " "    
if y == 'yes':
    charValues = name+string.digits+name+string.punctuation+name
    for i in range(pass_len):
     password += random.choice(charValues)
    print("Your Random password is =",password)
else:
    charValues = string.ascii_letters+string.punctuation+string.digits
    for i in range(pass_len):
        password += random.choice(charValues)
    print("Your random password is =",password)
print("\n This is a secure password which you can use")

