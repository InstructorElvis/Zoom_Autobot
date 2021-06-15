#Modules and Packages
#Core Python Modules like math
#Install Packages: camelCase, Django

#We will need some core and some installed packages/modules
#If you have buttons to click on the screen, you'll have to leverage another module that you have to install using pip called "pyautogui". 
import schedule
import time
import webbrowser

def open_link(link):
    webbrowser.open(link)


def intro_2_python():
    webbrowser.open("https://dfa.zoom.us/j/96815350328")

def aws_cloud_foundations():
    #Zoom Invite Link goes here: 
    awsZoomLink = ""

    #This will open your Zoom Invite Link
    webbrowser.open(f"{awsZoomLink}")

def elvis_room():
    webbrowser.open("https://us04web.zoom.us/j/2881787457?pwd=aUZHWlJncS8vL1FoTXlUcWJWaGN4UT09")

schedule.every().monday.at("10:30").do(aws_cloud_foundations)
schedule.every().tuesday.at("10:30").do(aws_cloud_foundations)
schedule.every().wednesday.at("10:30").do(aws_cloud_foundations)
schedule.every().thursday.at("10:30").do(aws_cloud_foundations)

#What am I gonna do if it's not the scheduled time?
while True:
    schedule.run_pending()
    print("Not Yet...")
    time.sleep(1)
