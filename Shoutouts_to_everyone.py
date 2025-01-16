"""
write a program to pronounce list of names using win32 api.

if you are given a list name as follows:

name = ["abdullah","nazmus", "sakib"]

your program should pronounce

Shoutout to abdullah
Shoutout to nazmus
Shoutout to sakib

"""

import pyttsx3


def pronounce_names(names):
    # Initialize the speech engine
    engine = pyttsx3.init()

    # Iterate through the names and pronounce them
    for name in names:
        message = f"Shoutout to {name}"
        print(message)  # Print the message
        engine.say(message)  # Queue the message for speaking

    # Run the speech engine
    engine.runAndWait()


# List of names
names = ["abdullah", "nazmus", "sakib"]

# Call the function
pronounce_names(names)