n=int(input("Enter number =>"))
n2=int(input("Enter number2 =>"))
c=0
for i in range (1,n+1):
    if i % n2==0:
        print(i)
        c+=1
print("Count =",c)  