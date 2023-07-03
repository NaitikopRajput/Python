tuple1=(12,23,34,45,56,67,78,89,90,99)
list1=list(tuple1)
c=0
sum=0
for x in list1:
    if x%7==0:
        print(x)
        c+=1
        sum+=x
    else:
        print()
        c+=1
        sum+=1
print("Sum Of All Values =",sum)
print("Total Count =",c)