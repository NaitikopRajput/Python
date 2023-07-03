print("Working Days Of School is equal to 365 days")
absent=int(input("Enter How much days You was absent =>"))
present=absent-365
per=absent/present*100
if per>75:
    print("You Can Give Exam")
else:
    print("You Can Not Give Exam")

