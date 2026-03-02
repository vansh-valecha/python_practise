a=int(input("enter 1st no:"))
b=int(input("enter 2nd no:"))   
o= input("enter operator:")
if(o=="+"):
 print("sum=",a+b)
elif(o=="-"):
    print("difference=",a-b)
elif(o=="*"):
    print("product=",a*b)
elif(o=="/"):
    if(b!=0):
     print("quotient=",a/b)
    else:
     print("division by zero is not allowed") 
else:    print("invalid operator")
