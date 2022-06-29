import platform
import time
import tkinter.messagebox
import psutil
# Importing these modules to assist in the development of this application. 



    
    
    



def checkifchargerispluggedin():
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
          tkinter.messagebox.showinfo("Battery Monitoro","Hello Windows User Welcome to the battery monitoring system")
      elif plat == "Linux":
          print("Hello Linux User Welcome to the battery monitoring system")
          
          # A function that fetches the operating system the user machine is running the program on. 
          
          
     



def main():
    counter = 0 # This counter has a special need in the program as it prevents the first condition from executing multiple times and therefore to improve user convenience 
  
    while True:
    # A while loop has been set to continously monitor the battery system on the machine 

        f = psutil.sensors_battery()
        # Stores the current battery percent after each iteration



        if f.percent == 100 and counter == 0 :
            tkinter.messagebox.showinfo("What a great day to start the day with 100%") 
            counter = counter + 1

            if counter > 0:
                continue

        elif checkifchargerispluggedin() == True:
            tkinter.messagebox.showinfo("The power cord is plugged in!")
        elif f.percent <= 50 and checkifchargerispluggedin() == False:


               tkinter.messagebox.showinfo("Advanced battery monitoro" , "Your battery is now currently at 50%. Please consider plugging your charger" )

        elif f.percent <= 30 and checkifchargerispluggedin() == False:
            tkinter.messagebox.showinfo("Please consider plugging in charger and consider backing up data! ")


        elif f.percent <= 20 and checkifchargerispluggedin() == False:
            tkinter.messagebox.showinfo("Your battery is critically low at a low {} ",format(f.percent))


        time.sleep(20)
        # This sleep timer has been implemented to allow the user to respond to the result of the program. The sleep time is set to 20 seconds but this has to  be manually customized 
        # TODO - Autommatically customize the timer function so that the user can choose the delay second. 
        












if __name__ == '__main__':
    getosversion() # Calling the getosversion to fetch the current version 
    main() #The main program gets executed here which contains the infinite looping code that checks the battery status in the system 
#Calls the two main functions so that the program can start!



