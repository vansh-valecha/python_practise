def show(n):
    if(n==0):
        return n
    print(n)
    show(n-1)
n=int(input("enter n:"))    
show(n)
