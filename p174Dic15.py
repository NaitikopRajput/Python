d1={1:40,2:49,3:30,4:9,5:50}
print("No\tName")
print("*"*30)
m=50
c=""
cf=0
cp=0
for k,v in d1.items():
    if v<30:
        c="Fail"
        cf+=1
    else:
        c="Pass"
        cp+=1
print(k,"\t",v,"\t",m,"\t",c)


print("*"*30)  
print("Count Of Pass =",cp)
print("Count Of Fail =",cf)
