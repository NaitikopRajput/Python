import random
y=random.randint(1,20)
x=random.randint(1,20)
print("Number 1 =",y)
print("Number 2 =",x)

Answer=int(input("What is addition of both number ? =>"))

if Answer==y+x:
    print("It is correct Answer")
else:
    print("It is incorrect Answer")