#wap to find factorial of n no
n = int(input("enter no : "))
fact = 1
for i in range(1, n + 1,1):
    fact = fact * i
print("factorial is", fact) 
