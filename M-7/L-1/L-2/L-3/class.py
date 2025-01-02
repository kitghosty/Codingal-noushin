# if statement
age = 18
if age >= 18:
    print("You are eligibe to vote!")

# if-else statement
number = 5
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# if-else-elif statement
marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")

number = 10
if number > 0:
    if number % 2 == 0:
        print("Postive even number")
    else:
        print("Positive odd number")
else:
    print("Not a positive number")


import datetime

#Current Date and Time
currentTime = datetime.datetime.now()
print("Current Date and Time:", currentTime)

#Extracting date and time
print("Year:", currentTime.year)
print("Month:", currentTime.month)
print("Day:", currentTime.day)
print("Hour:", currentTime.hour)
print("Minute:", currentTime.month)
print("Second", currentTime.second)

# Formatting date and time
formatted_time = currentTime.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted Date and Time:", formatted_time)