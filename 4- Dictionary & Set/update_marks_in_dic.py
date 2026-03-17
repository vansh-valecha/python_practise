#wap print marks of 3 sub in dictionary
info={}
chem=int(input("enter marks of chem:"))
phy=int(input("enter marks of phy:"))
math=int(input("enter marks of math:"))
info.update({"chem":chem})
info.update({"phy":phy})
info.update({"math":math})
print(info)
