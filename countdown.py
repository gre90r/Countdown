"""
    counts down minutes and wakes when counter reaches zero
    @date april 2020
    @author gre90r
"""

from time import sleep
from sys import exit
import logic

# init
seconds = int(0)
functions = logic.Logic()

# user input
eventname = str(input("event name: "))
minutes = functions.getInputMinutes()
notification = functions.getNotificationInput()

# user info
print("press CTRL+C to quit")

# mainloop
try:
    while minutes > 0 or seconds > 0:
        print('{:02d}:{:02d} remaining'.format(minutes, seconds))
        seconds = seconds - 1
        if seconds < 0:
            seconds = 59
            minutes = minutes - 1
        sleep(1)

    # countdown reached zero
    print('{:02d}:{:02d} remaining'.format(minutes, seconds))
    functions.notifyUser(notification, eventname)
except KeyboardInterrupt:
    """ when user presses CTRL+C to exit """
    print("countdown aborted")
    exit(0)
except Exception as err:
    """ unknown error """
    print(err)
    exit(99)
