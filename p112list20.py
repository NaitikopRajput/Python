list1=[1,2,3,4,5,5,7,8,3]
ce=0
co=0
c=0
so=0
se=0
s=0
for x in list1:
    if x%2==0:
        print(x,"Is even")
        ce+=1
        c+=1
        se+=x
        s+=x
    else:
        print(x,"Is Odd")
        co+=1
        c+=1
        so+=x
        s+=x
print("Total Number Of Items In list waas =",c)
print("Total Number Of Items Even In list waas =",ce)
print("Total Number Of Items Odd In list waas =",co)
print("Sum Of all Values =",s)
print("Sum Of Evens =",se)
print("Sum Of Odds =",so)
