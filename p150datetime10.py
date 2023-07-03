import time
current=time.localtime(time.time())
hour=current.tm_hour
if hour>12:
    print("PM")
else:
    print("AM")
