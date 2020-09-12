"""
    @author gre90r
"""

from tkinter import Tk, messagebox
from datetime import datetime

class Logic:
    def __init__(self):
        pass

    def validateMinutes(self, minutes):
        """ check the user input minutes """
        if type(minutes) not in [int]:
            raise ValueError("minutes must be a number")
        if minutes < 1:
            raise ValueError("minutes must be a number greater 0")

    def validateNotification(self, n):
        """ check if notification is either y or n """
        if not (n == "y" or n == "n"):
            raise ValueError("messagebox notification must be either y or n") 

    def notifyUser(self, n, e):
        """ notify user that countdown reached zero
            @param n = notification
            @param e = eventname
        """
        if n == "y":
            """ show messagebox """
            root = Tk()
            root.withdraw() # hide mainwindow, so only messagebox is displayed
            messagebox.showinfo("countdown", 'event ' + e.upper() + ' is now')
        elif n == "n":
            """ show message in console """
            print(e.upper() + " event is now", self.getCurrentTime())
        else:
            print("error: unknown notification. ahem, anyways. your countdown finished",
                self.getCurrentTime())

    def getCurrentTime(self):
        """ get current time in format hh:mm:ss -> 21:46:12"""
        now = datetime.now()
        return now.strftime("%H:%M:%S")

    def getInputMinutes(self):
        try:
            minutes = int(input("enter a time in minutes: "))
        except ValueError:
            """ wrong type """
            print("!!! enter a number for minutes !!!")
            exit(1)
        try:
            self.validateMinutes(minutes)
        except ValueError as err:
            """ out of range. because it is negative """
            print("!!!", err, "!!!")
            exit(2)
        return minutes

    def getNotificationInput(self):
        notification = str(input("messagebox notification (y/n): "))
        try:
            self.validateNotification(notification)
        except ValueError as err:
            """ notification was not y or n """
            print("!!!", err, "!!!")
            exit(3)
        return notification
