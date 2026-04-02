#wap to calculate sum of first n natural number
def sum(n):
    if(n==0):
        return n
    return n+sum(n-1)
n=int(input("enter n:"))
print(sum(n))
