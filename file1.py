# Import Module
import string
import random
# Password Length
PassLength=int(input("Enter the Length of the Password:"))

print("""Choose Character set for password from those
         1.Letter
         2.digits
         3.Special Characters
         4.Exit""")
# creating a empty variable string
character=''
# using while loop 
while(True):
     choose=int(input("Enter the number:"))
     # Letter
     if (choose==1):
        character+=string.ascii_letters
     # Digit
     elif(choose==2):
         character+=string.digits
     # Special Character
     elif(choose==3):
        character+=string.punctuation
     # exit
     elif(choose==4):
       break
     # Invaild option
     else:
         print("please select the correct option:")
# Creating a list 
password=[]

for i in range(0,PassLength):
# picking the randomcharacter from our choices
    randomchart=random.choice(character)
#   appending the randomchart to password
    password.append(randomchart)
print("The random password is:"+"".join(password))
