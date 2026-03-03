a=int(input("enter 1st no :"))
b=int(input("enter 2nd no :"))
c=int(input("enter 3rd no :"))
if(a==b==c or a==b!=c or a!=b==c):
 print("number are equal")
else:
 if(a>b):
    if(a>c):
     print("a is greatest")
    else:
     print("c is greatest")
 elif(a<b):
    if(b>c):
     print("b is greatest")
    else:
     print("c is greatest")
