import random
Q=int(input("How much Questions You will answer =>"))
i=1
cc=0
ci=0
for o in range(1,Q+1):
    y=random.randint(1,20)
    x=random.randint(1,20)
    print("Number 1 =",y)
    print("Number 2 =",x)

    Answer=int(input("What is addition of both number ? =>"))

    if Answer==y+x:
        print("It is correct Answer")
        cc+=1
    else:
        print("It is incorrect Answer")
        ci+=1
print("Correct =",cc)
print("Incorrect =",ci)