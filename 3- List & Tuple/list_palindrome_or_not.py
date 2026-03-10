wap a progra to check if list is palandreome or not
list1 =[1,2,3,2,1]
copy_list1 = list1.copy()
list1.reverse()
if(list1==copy_list1):
    print("list is palandreome")
else:
    print("list is not palandreome")
