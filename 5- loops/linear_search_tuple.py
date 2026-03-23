#wap to search a no in tuple
num=(1,4,9,16,25,36,49,81,100)
n=int(input("enter no to search:"))
i=0
while i<=(len(num)-1): #i<=8
    if (num[i]==n):
        print("no found at",i+1)
    else: 
        print("no not found")  
    i+=1  
