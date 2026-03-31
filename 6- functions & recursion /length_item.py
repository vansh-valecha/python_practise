# wap to print leangth of list & item using function
cities=["noida","delhi","meerut","pune","hyderabad"]
movie=["dhurandar","animal","kgf"]

def length ( list ):
    print("length of list:",len(list))
def check(list):
    for item in list:
        print(item,end=" ")
        
length(cities) 
check(cities)
print("\n")
length(movie)
check(movie) 
