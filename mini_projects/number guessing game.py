import random
secret=random.randint(1,100)
while True:
    guess=int(input("Enter the guessing number"))
    if guess>secret:
        print("The guessing number is too long")
    elif guess<secret:
        print("The guessing number is too small")
    elif guess==secret:
        print("The guessing number is same")
        break
    else:
        print("Try again")
