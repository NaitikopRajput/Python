import time
current=time.localtime(time.time())
hour=current.tm_hour
if hour>12:
    print("Good Evening")
elif hour<12:
    print("Good Morning")
else:
    print("Good Night")
