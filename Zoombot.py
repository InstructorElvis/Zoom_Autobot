#Modules and Packages
#Core Python Modules like math
#Install Packages: camelCase, Django

#We will need some core and some installed packages/modules
#If you have buttons to click on the screen, you'll have to leverage another module that you have to install using pip called "pyautogui". 
import schedule
import time
import webbrowser

#Pass in any link to this function to have it open that link on the webbrowser.
def open_link(link):
    webbrowser.open(link)


def intro_2_python():
    intro2Python = ""
    webbrowser.open(f"{intro2Python}")

def aws_cloud_foundations():
    #Zoom Invite Link goes here: 
    awsZoomLink = ""

    #This will open your Zoom Invite Link
    webbrowser.open(f"{awsZoomLink}")

    
#Use the schedule module in order to leverage its method to schedule your function to run at a certain time. 

schedule.every().monday.at("10:30").do(aws_cloud_foundations)
schedule.every().tuesday.at("10:30").do(aws_cloud_foundations)
schedule.every().wednesday.at("10:30").do(aws_cloud_foundations)
schedule.every().thursday.at("10:30").do(aws_cloud_foundations)

#What am I gonna do if it's not the scheduled time?
#Create an infinite loop that will run until the time is met. 
while True:
    schedule.run_pending()
    print("Not Yet...")
    time.sleep(1)
