#for fy 2025-2026[AY(2026-2027)]
income=int(input("enter your income:"))
if(income<=400000):
    print("no tax")
elif(income<=800000):
    tax=0.05*income
    print("tax to be paid:",tax)
elif(income<=1200000):
    tax=0.1*income
    print("tax to be paid:",tax)
elif(income<=1600000):
    tax=0.15*income
    print("tax to be paid:",tax)
elif(income<=2000000):
    tax=0.2*income
    print("tax to be paid:",tax)
else:
    tax=0.3*income
