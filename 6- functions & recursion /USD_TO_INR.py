#wap to convert usd in inr
def currency(n):
    c=n*94.21
    return c
n=int(input("enter amount:"))
print(n,"USD  =",currency(n),"INR")
