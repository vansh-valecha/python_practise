#find the element in the list & print the position.
LIST=[1,4,9,16,25,36,49,64,81,100]
x=int(input("enter no to be search:"))
i=0
for el in LIST:
    if(x == el):
     print("element found",i+1)
    i+=1     
