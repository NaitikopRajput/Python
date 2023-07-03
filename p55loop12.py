n=int(input("Enter number =>"))
c=0
s=0
for i in range (1,n+1):
    if i%2==0:
        print(i)
        c+=1
        s=s+i
print("Count =",c)
print("Sum =",s)