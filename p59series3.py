n=int(input("Enter limit =>"))
s=0
for i in range(1,n+1):
    i=i*i
    print(i," + " ,end=" ")
    s+=i

print("\nSum = ",s)