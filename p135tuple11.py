tuple1=(12,23,34,45,56,67,78,89,90,99)
list1=list(tuple1)
c=0
ce=0
co=0
for x in list1:
    if x%2==0:
        print(x)
        ce+=1
        c+=1
    else:
        print()
        co+=1
        c+=1
print("Count Of Even Values =",ce)
print("Count Of Odd Values =",co)
print("Total Count =",c)