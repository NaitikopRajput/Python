d1={1:40,2:49,3:30,4:9,5:50}
print("No\tName")
print("*"*30)
m=50
c=""
for k,v in d1.items():

    if v<30:
        c="Fail"
    else:
        c="Pass"
    if c=="Pass":
       print(k,"\t",v,"\t",m,"\t",c)
    else:
        print()
print("*"*30)  