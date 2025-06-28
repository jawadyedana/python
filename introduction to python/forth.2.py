import datetime 
# Current date and time 
#              module.class.method()
currentTime = datetime.datetime.now()
print("Current Date and Time:, currentTime")

# Extracting date and time 
print("Year:", currentTime.year)
print("Month:", currentTime.month)
print("Day:", currentTime.day)
print("Hour:", currentTime.hour)
print("Minute:", currentTime.minute)
print("Second:", currentTime.second)

# Formatting date and time 
formatted_time = currentTime.strftime("%d-%m-%Y %H:%M:%5")
print("Formatted Date and Time:", formatted_time)
