import random

n=int(input("Enter limit =>"))
d1={}
for i in range(1,n+1):
    rno=random.randint(1,50)
    mark=random.randint(1,50)
    d1[rno]= mark

print(d1)

print("Press 1 to get data of passed students")
print("Press 2 to get data of Failed students")
print("Press 3 to get data of Both students")
cp=0
cf=0
opt=int(input("Enter Option =>"))
if opt==1:
    if mark>30:
        cp+=1
        print(d1)
if opt==1:
    if mark<30:
        print()
if opt==2:
    if mark<30:
        cf+=1
        print(d1)
if opt==2:
    if mark>30:
        print()
if opt==3:
    print(d1)
print("Count Pass",cp)
print("Count Fail",cf)

