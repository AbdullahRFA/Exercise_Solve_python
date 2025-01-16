"""
Write a python program which reminds you of drinking water every hour or two.
Your program can either beep or send desktop notifications for a specific operating system like mac

"""

import os

import time

REPEAT_INTERVAL = 10 #repeat frequency in seconds

while True:
    command = "osascript -e \'say \"Hey Abdullah Drink Water\"\'; osascript -e \'display alert \"Hey Abdullah Drink Water\"\'"
    os.system(command)
    time.sleep(REPEAT_INTERVAL)

