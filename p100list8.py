list1=[1,2,3,4,5,5,7,8,3]
ce=0
co=0
c=0
for x in list1:
    if x%2==0:
        print(x,"Is even")
        ce+=1
        c+=1
    else:
        print(x,"Is Odd")
        co+=1
        c+=1
print("Total Number Of Items In list waas =",c)
print("Total Number Of Items Even In list waas =",ce)
print("Total Number Of Items Odd In list waas =",co)