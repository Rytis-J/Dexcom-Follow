import imaplib
import time
import os
from playsound import playsound
from pydexcom import Dexcom
import smtplib
from email.mime.text import MIMEText



#dexcom name
dexcomname = "name"

#dexcom password
dexcompassword = "password"

#Email
useremail ="Your_email_adress@gmail.com"

#Email password
email_password= "Email Password"

# Set alerts
high_glucose = 10 #script is going to play alert sound if blood sugar levels are going to reach this level

low_glucose = 4 #script is going to play alert sound if blood sugar levels are going to go below this level

# By setting this option to True, you are going to receive alerts if your blood sugar levels are going to exceed the set range  (glucose > high_glucose or glucose < low_glucose) 
sounds = True

# If True, you will receive emails only if your sugar levels are going to be out of range (glucose > high_glucose or glucose < low_glucose) 
glucose_out_of_range = False

# to do list

send_email_every_x_minutes = 5 #input time you wait to wait before a new email (Dexcom sends updates every 5 minutes so setting value to less then 5 is not recommended)

# for mmol/l set to false, for mg/dl set to true
mg_dl = False

# Account registered location true if USA, False if outside USA
region = False






#code |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def front():
    os.system('cls||clear')
    print("████████╗░█████╗░░██████╗░███████╗████████╗██╗░░██╗███████╗██████╗░  ░██╗░░░░░░░██╗███████╗  ░█████╗░░█████╗░███╗░░██╗")
    print("╚══██╔══╝██╔══██╗██╔════╝░██╔════╝╚══██╔══╝██║░░██║██╔════╝██╔══██╗  ░██║░░██╗░░██║██╔════╝  ██╔══██╗██╔══██╗████╗░██║")
    print("░░░██║░░░██║░░██║██║░░██╗░█████╗░░░░░██║░░░███████║█████╗░░██████╔╝  ░╚██╗████╗██╔╝█████╗░░  ██║░░╚═╝███████║██╔██╗██║")
    print("░░░██║░░░██║░░██║██║░░╚██╗██╔══╝░░░░░██║░░░██╔══██║██╔══╝░░██╔══██╗  ░░████╔═████║░██╔══╝░░  ██║░░██╗██╔══██║██║╚████║")
    print("░░░██║░░░╚█████╔╝╚██████╔╝███████╗░░░██║░░░██║░░██║███████╗██║░░██║  ░░╚██╔╝░╚██╔╝░███████╗  ╚█████╔╝██║░░██║██║░╚███║")
    print("░░░╚═╝░░░░╚════╝░░╚═════╝░╚══════╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝  ░░░╚═╝░░░╚═╝░░╚══════╝  ░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝")

    print("██████╗░███████╗░█████╗░████████╗  ██████╗░██╗░█████╗░██████╗░███████╗████████╗███████╗░██████╗██╗")
    print("██╔══██╗██╔════╝██╔══██╗╚══██╔══╝  ██╔══██╗██║██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝██║")
    print("██████╦╝█████╗░░███████║░░░██║░░░  ██║░░██║██║███████║██████╦╝█████╗░░░░░██║░░░█████╗░░╚█████╗░██║")
    print("██╔══██╗██╔══╝░░██╔══██║░░░██║░░░  ██║░░██║██║██╔══██║██╔══██╗██╔══╝░░░░░██║░░░██╔══╝░░░╚═══██╗╚═╝")
    print("██████╦╝███████╗██║░░██║░░░██║░░░  ██████╔╝██║██║░░██║██████╦╝███████╗░░░██║░░░███████╗██████╔╝██╗")
    print("╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░  ╚═════╝░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝░░░╚═╝░░░╚══════╝╚═════╝░╚═╝")
    print("_______________________________________________________\n")

front()
time.sleep(2)


def lines():
    print("_______________________________________________________\n")

def dexcomnamelogin():
    n = input("Dexcom Name: ")
    return n
def dexcompass():
    n = input("Dexcom Password: ")
    return n

dexcominfo = []

def dexcomlogin(dexcomname, dexcompassword):
    front()
    try:
        __init__ = Dexcom(dexcomname, dexcompassword, ous=True)
        dexcom = Dexcom(dexcomname, dexcompassword, ous=True)
        bg = dexcom.get_current_glucose_reading()
        front()
        print("Successfully logged in to dexcom!")
        lines()
        time.sleep(4)
        front()
    except:
        front()
        print("Username:", dexcomname)
        print("Password:", dexcompassword)
        print("")
        print("Your name or password is incorrect. Please try again!")
        lines()
        dexcomname = dexcomnamelogin()
        dexcompassword = dexcompass()
        dexcomlogin(dexcomname, dexcompassword)
    dexcominfo.append(dexcomname)
    dexcominfo.append(dexcompassword)
dexcomlogin(dexcomname, dexcompassword)
dexcomname = dexcominfo[0]
dexcompassword = dexcominfo[1]

def lines():
    print("_______________________________________________________\n")
#credentials
username = useremail

#generated app password
app_password= email_password

lines()
# https://www.systoolsgroup.com/imap/
gmail_host= 'imap.gmail.com'

#set connection
mail = imaplib.IMAP4_SSL(gmail_host)

emaildetails = []

def emailname():
    username = input("E-mail: ")
    return username
def emailpassword():
    app_password = input("Email Password: ")
    return app_password



def login(username, app_password):
    front()
    try:
        print("Email address:", username)
        print("Password:", app_password)
        mail.login(username, app_password)
        front()
        print(f"Successfully loged in to your email!")
        lines()
    except:
        print("")
        print("The email address or password is incorrect. Please try again!")
        lines()
        username = emailname()
        print("")
        app_password = emailpassword()
        login(username, app_password)
    emaildetails.append(username)
    emaildetails.append(app_password)


def dexcomfollow(username, app_password):
    front()
    print("Dexcom data following by email was started!")
    if glucose_out_of_range == True:
        print()
        print(f"Emails will only be sent if glucose is going to be out of the set range (Higer then {high_glucose} or lower then {low_glucose})")
    lines()
    def currentglucose():
        __init__ = Dexcom(dexcomname, dexcompassword, ous=region)
        dexcom = Dexcom(dexcomname, dexcompassword, ous=region)
        bg = dexcom.get_current_glucose_reading()
        if mg_dl == False:
            return bg.mmol_l
        else:
            return bg.mg_dl

    def sendemail(receiver, username, app_password):
        __init__ = Dexcom(dexcomname, dexcompassword, ous=region)
        dexcom = Dexcom(dexcomname, dexcompassword, ous=region)

        # ous=True# add ous=True if outside of US
        bg = dexcom.get_current_glucose_reading()
        listas = []
        if mg_dl == False:
            listas.append(bg.mmol_l)
        else:
            listas.append(bg.mg_dl)
        listas.append(bg.trend_description)
        listas.append(bg.trend_arrow)        


        smtp_ssl_host = gmail_host
        smtp_ssl_port = 465
        password = app_password
        sender = username
        targets = [receiver]
        print("Sent to:", receiver, f"Current blood sugar levels: {listas[0]}")
        # correct = correction(listas[0])
        msg = MIMEText(f'Current dexcom readings:\nLatest glucose reading:{listas[0]}\ntrend_description: {listas[1]}, {listas[2]}\n')
        msg['Subject'] = 'Hello'
        msg['From'] = sender
        msg['To'] = ', '.join(targets)

        server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
        server.login(username, password)
        server.sendmail(sender, targets, msg.as_string())

    def mails():
        with open('mails.txt') as f:
            lines = f.readlines()
            return lines

    userlist = mails()

    def sendtosubscribers():
        for x in userlist:
            if glucose_out_of_range == True:
                if currentglucose() > high_glucose or currentglucose() < low_glucose:
                    sendemail(x, username, app_password)
                    lines()
            else:
                sendemail(x, username, app_password)
                lines()

    def noemails():
        front()
        print("No emails where provided! (mails.txt)")
        lines()
        time.sleep(5)

    if len(userlist) == 0:
        noemails()
        os.system('cls||clear')
        options()

    lastscan = None

    while True:
        glucose = currentglucose()
        if glucose != lastscan:
            lastscan = glucose
            sendtosubscribers()
            print(f"I'll wait {send_email_every_x_minutes} minutes, and if the glucose is going to change I will send an email.")
            time.sleep(send_email_every_x_minutes*60)
            print("check")

        else:
            time.sleep(10)

    timing()


def live():
    lastscan = 0
    refreshtime = 10
    front()
    print(f"Live dexcom data! Refreshes every {refreshtime} seconds:")
    
    if mg_dl == False:
        while True:
            __init__ = Dexcom(dexcomname, dexcompassword, ous=True)
            dexcom = Dexcom(dexcomname, dexcompassword, ous=True)
            bg = dexcom.get_current_glucose_reading()
            try:

                arrow = bg.trend_arrow
                if bg.mmol_l != lastscan:
                    front()
                    print(f"Live dexcom data! Refreshes every {refreshtime} seconds:")
                    lastscan = bg.mmol_l
                    print('\033[1m')
                    print("Current glucose:", bg.mmol_l, arrow)
                    print('\033[0m')
                    if sounds == True:
                        def function_sound():
                            playsound('sound.mp3')
                        if lastscan > high_glucose or lastscan < low_glucose:
                            function_sound()

            except Exception as e:

                if(not bg):
                    print("Failed to fetch the latest datascan from Dexcom, make sure you have readings on the official Dexcom app.")
                else:
                    print("Error while playing alert sound")
                    
                
            time.sleep(refreshtime)

    else:
        while True:
            __init__ = Dexcom(dexcomname, dexcompassword, ous=True)
            dexcom = Dexcom(dexcomname, dexcompassword, ous=True)
            bg = dexcom.get_current_glucose_reading()
            try:
                arrow = bg.trend_arrow

                if bg.mg_dl != lastscan:
                    front()
                    print(f"Live dexcom data! Refreshes every {refreshtime} seconds:")
                    lastscan = bg.mg_dl
                    print('\033[1m')
                    print("Current glucose:", bg.mg_dl, arrow)
                    print('\033[0m')
                    if sounds == True:
                        def function_sound():
                            playsound('sound.mp3')
                        if lastscan > high_glucose or lastscan < low_glucose:
                            function_sound()

            except Exception as e:

                if(not bg):
                    print("Failed to fetch the latest datascan from Dexcom, make sure you have readings on the official Dexcom app.")
                else:
                    print("Error while playing alert sound")
                    
        
            time.sleep(refreshtime)
        


def options():
    front()
    print("Choose an option by typing in a number in the input field:\n")
    print("[1] Live glucose")
    print("[2] Dexcom follow by email\n")
    n = input("Option: ")
    if n == "1":
        front()
        live()
    elif n == "2":
        if len(useremail) == 0:
            username = emailpassword()
            front()
            lines()
        else:
            username = useremail

        if len(email_password) == 0:
            app_password = emailpassword()
            front()
        else:
            app_password = email_password

        print("Email:", username)
        print("Password:", app_password)

        login(username, app_password)
        time.sleep(2)
        front()
        username = emaildetails[0]
        app_password = emaildetails[1]
        print(username)
        dexcomfollow(username, app_password)
    else:
        front()
        print(f"Couln't recognize your input: {n}. Please try again!\n")
        lines()
        options()


options()

# developed by Rytis-J https://github.com/Rytis-J/dexcomfollow