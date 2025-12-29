##Get value from user
Name=input("Enter the Name :")
Age=input("Enter the age :")
print("The name and age are :",Name,Age) 
##single line output
print("The name and age are  ", input("enter the name"), input("Enter the age"))
##Using f-string
print(f"The name and age are: {input("name")} {input("age")}")
##Using walrus operator
print(f"The name and agr are: {(n:=input("Name"))} {(a:=input("Age"))} ")
 