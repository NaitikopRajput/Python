import random
n=int(input("Enter limit =>"))
d1={}
for i in range(1,n+1):
    rno=random.randint(1,50)
    mark=random.randint(1,50)
    d1[rno]=mark
print(d1)
rollno=int(input("Enter Roll No."))
