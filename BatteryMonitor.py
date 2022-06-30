import platform
import time
import tkinter.messagebox
import psutil


# Importing these modules to assist in the development of this application.

def checkifchargerisplugg():
    plugged = False

    if psutil.sensors_battery().power_plugged == True:
        plugged = True

    if plugged == True:
        return True
    else:
        return False


# A function that detects if a poweradapter is plugged into the system

def getosversion():
    plat = platform.system()
    if plat == "Windows":
        tkinter.messagebox.showinfo("Battery Monitoro", "Hello Windows User Welcome to the battery monitoring system!")
    elif plat == "Linux":
        tkinter.messagebox.showinfo("Battery Monitoro", "Hello Linux  User to the battery monitoring system!")

        # A function that fetches the operating system the user machine is running the program on.


def main():
    counter = 0# This counter has a special need in the program as it prevents the first condition from executing multiple times and therefore to improve user convenience
    powercounter = 0 #The power counter stops the need for the power is plugged in condition to keep executing as when the power counter is larger than zero,  it just continues the iteration which prevents the messagebox from appearing again and again.
    while True:
        # A while loop has been set to continously monitor the battery system on the machine

        f = psutil.sensors_battery()
        # Stores the current battery percent after each iteration

        if f.percent == 100 and counter == 0:
            tkinter.messagebox.showinfo("Advanced battery monitoro", "What a great day to start the day with 100%!")
            counter = counter + 1

            if counter > 0:
                continue

        elif checkifchargerisplugg() == False and powercounter == 0:
            tkinter.messagebox.showinfo("Advanced battery monitoro", "Power plugged in")
            powercounter = powercounter + 1

            if powercounter > 0:
                continue
        elif f.percent <= 50 and checkifchargerisplugg() == False:
            powercounter = 0

            tkinter.messagebox.showinfo("Advanced battery monitoro",
                                        "Your battery is now currently at 50%. Please consider plugging your charger")
            
        

        elif f.percent <= 30 and checkifchargerisplugg() == False:
           powercounter = 0
           tkinter.messagebox.showinfo("Advanced battery monitoro","Please consider plugging in charger and consider backing up data! ")
            
        elif f.percent <= 20 and checkifchargerisplugg() == False:
            powercounter = 0
        tkinter.messagebox.showinfo("Advanced battery monitoro","Please consider plugging in charger and consider backing up data! ")
        

       
# These conditions monitor the status of the battery regularly and report it to the user as soon as something has occured.

time.sleep(20)
# This sleep timer has been implemented to allow the user to respond to the result of the program. The sleep time is set to 20 seconds but this has to  be manually customized
# TODO - Autommatically customize the timer function so that the user can choose the delay second.
# TODO- Add customization so that the user can choose whether to add the application to startup. To add this we need add a function called isstartup and make it to return a value like a True or a false depending on the user choice.
# TODO- NEED TO FIX FORMATTING and add  a better messagebox reply back to the user!
# TODO - ADD A RANDOM QUOTE GENERATOR
















