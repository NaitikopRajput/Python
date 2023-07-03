num=int(input("Enter Number =>"))
r_num=0
temp=num

while num !=0:
    digit=num%10
    r_num = r_num*10+digit
    num//=10

print("Reversed Number =>", r_num)

if temp==r_num:
    print("It is palindrome number")
else:
    print("It is not palindrome number")
