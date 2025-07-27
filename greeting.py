from datetime import datetime

hour = datetime.now().hour
name = input("enter your name ")
name = name.capitalize()
if hour < 12:
    print("Good Morning", name)
elif 12 <= hour < 17:
    print("Good Afternoon", name)
elif 17 <= hour < 21:
    print("Good evenung", name)
else:
    print("Good Night", name)
