### Login Validation System
#A simple Python program that verifies user login credentials.  
#It allows up to 3 attempts and locks the account after failed attempts.  
#This project demonstrates the use of loops, conditions, and string comparison.

for i in range(3):
    print(f"Enter the {i+1} credentials:")
    username=input("Enter the username: ")
    password=int(input("Enter the password: "))

    if username == "ezhil" and password == 1234:
        print("login is Successful")
        break
    else:
        print("Entered wrong credentials try again")
        
else:
    print("Your account was locked")
