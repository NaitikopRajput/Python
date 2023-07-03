n=int(input("Enter number =>"))
ce=0
co=0
for i in range (1,n+1):
    if i % 2==0:
        print(i,"is even")
        ce+=1
    else:
        print(i,"is odd")
        co+=1

print("Count Enven =",ce)
print("Count Odd =",co)
   