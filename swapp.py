print("Entered the number :" ,(a:=int(input( "number1"))))
print("Entered the number :" ,(b:=int(input( "number2"))))
print("Before swapping a and b", a ,b)
##Using third variable
temp=a
a=b
b=temp
print("after swapping a and b :", a,b)
##Without  third vaariable
x,y=a,b
x=x+y
y=x-y
x=x-y
print("after swapping", x,y)
##using pythonic way
a,b=b,a
print("after swapping", a,b)