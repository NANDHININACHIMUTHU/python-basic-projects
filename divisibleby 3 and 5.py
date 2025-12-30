number=float(input("enter the number"))
if number%3==0 and number%5==0:
    print("the number is both divisible by 3 and 5")
elif number%3==0 or number%5==0:
    print("The number divisle by any one")
else:
    print("the number is not divisible by 3 nad 5")