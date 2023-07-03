tuple1=(11,22,33,44,555,66,77,88,99,100)
inte=int(input("Guess a number from tuple =>"))
for item in tuple1:
    if inte==item:
        print(item)
    else:
        print()