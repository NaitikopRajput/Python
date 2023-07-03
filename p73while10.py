num=123456789
r_num=0

while num !=0:
    digit=num%10
    r_num = r_num*10+digit
    num//=10

print("Reversed Number =" + str(r_num))