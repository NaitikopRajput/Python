import random

pclist=["stone","papper","sicssors"]

selectedword=random.choice(pclist)

userword=int(input("Enter =>"))
upoint=0
ppoint=0

print("yours =",userword)
print("mine =",selectedword)

if userword=="sicssors" and selectedword=="sicssors":
    print("Same!")
elif userword=="stone" and selectedword=="stone":
    print("Same")
elif userword=="papper" and selectedword=="papper":
    print("Same!")
elif userword=="sicssors" and selectedword=="papper":
    print("your point")
    upoint+=1
elif userword=="papper" and selectedword=="stone":
    print("your point")
    upoint+=1
elif userword=="stone" and selectedword=="sicssors":
    upoint+=1
elif userword=="sicssors" and selectedword=="stone":
    ppoint+=1
elif userword=="stone" and selectedword=="papper":
    ppoint+=1
elif userword=="papper" and selectedword=="sicssors":

if 