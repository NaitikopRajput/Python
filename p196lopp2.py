
lower = int(input("Enter Lower =>"))
upper = int(input("Enter Upper =>"))

print("Prime numbers between", lower, "and", upper, "are:")
c=0
for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
           c+=1
print("Count =",c)
