print("1 pizza = 300rs")
pizza=int(input("How many pizza do you want to eat?  =>"))
bill=pizza*300
print("Bill =",bill)
if bill<1000:
    print("pay cash")
else:
    print("You can pay with card also")