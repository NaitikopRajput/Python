import datetime
today = datetime.date.today()
birthDate = datetime.date(2003, 10, 16)
age = today.year - birthDate.year
print(age)