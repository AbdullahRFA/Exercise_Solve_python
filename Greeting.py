"""
create a program capable for greeting you good morning, good afternoon, good evening,
good night by using time module

"""
from time import strftime

t= strftime('%H:%M:%S')
hour = int(strftime("%H"))

print("Time : ",t)

if 0 <= hour < 12:
    print("Good Morning!")
elif 12 <= hour < 16:
    print("Good Afternoon!")
elif 16 <= hour < 20:
    print("Good Evening!")
elif 20 <= hour < 0:
    print("Good Night!")

