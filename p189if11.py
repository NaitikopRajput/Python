month = int(input("Enter the month number =>"))
year = int(input("Enter the year =>"))

if year%4==0:

    if month == 2:
        print("28 days")
    else:
        print("29 days")
   
elif month in [4, 6, 9, 11]:
    print("30 days")
else:
    print("31 days")
