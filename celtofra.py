value=int(input("enter the cel=0 or fra=1"))
if value==0:
    cel=int(input("Enther the celsius value"))
    fr=(cel*9/5)+32
    print("fahrenheit value", fr)
else:
    fah=int(input("enter the fahrenhit value"))
    c=(fah-32)*5/9
    print("celsius value",c)
    