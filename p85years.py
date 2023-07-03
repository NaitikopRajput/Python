days=int(input("Enter Number Of Days =>"))
year=days//365
Mounth=(days%365)//30
Days=(days%365)%30
print("Year =",year,"Mounths =",Mounth,"Days =",Days)