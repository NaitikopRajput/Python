def add(*y):
    c=0
    s=0
    for x in y:
        if x%2==0:
            c+=1
            s+=x
            print(x)
    print("count =",c)
    print("sum =",s)
add(1,2)
add(1,2,3)
add(1,2,3,4)
add(1,2,3,4,5)