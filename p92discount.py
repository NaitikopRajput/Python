price=int(input("Enter Price =>"))

if price>10000:
    print("You Will Get 20% Discount")
    print("You Now Have to pay",price-0.20)
elif price>7000 and price<10000:
     print("You Will Get 15% Discount")
     print("You Now Have to pay",price-0.15)
elif price<7000: 
     print("You Will Get 10% Discount")
     print("You Now Have to pay",price-0.10)