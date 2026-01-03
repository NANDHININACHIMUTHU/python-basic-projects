year=int(input("ENTER THE YEAR"))
if (year%4==0 and year%100!=0) or(year%400==0):
        print("leap year")
else:
        print("Not leap year")
