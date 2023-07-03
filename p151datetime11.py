import datetime
now = datetime.datetime.now()
current_time = now.strftime("%I:%M:%S %p")
print(f"The current time is {current_time}")