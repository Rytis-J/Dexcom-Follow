# Dexcom-follow
Have an issue with your Dexcom Follow app? Or maybe you just want to get your Dexcom data/receive alerts on your computer?! Get your live Dexcom data via email, live in your Command Prompt!

# Why?
1. Many Dexcom users are having trouble using Dexcom Follow due to various circumstances. For some, they have incompatible devices for others it's a software glitch. I came up with the idea to help people with these problems. For this problem, I created **Mode [2] Subscribe to the latest data with your email**. No matter what device you are using, as long as there is an emailing system in it, you're good to go! You will receive a detailed email with the latest glucose reading!
```
Current dexcom readings:
Latest glucose reading: 5.4
trend_description: steady, →
```
**Note:** to change it to mg/dL check out settings tab.

2. I always wanted to see my Dexcom data on my computer. As of now, there is no way to see your data on it. Sometimes when you're working with your headphones on, it's hard to hear alerts! That's why I developed **Mode [1] Live Glucose**. You can set alerts within the script so you could receive a *Beeep* if your sugar levels are out of range ;-) 

# Setup
  If not installed, install Python 3, Git - https://www.python.org/downloads/, https://git-scm.com/book/en/v2/Getting-Started-Installing-Git.
  ```
  git clone https://github.com/Rytis-J/dexcomfollow.git
  ```
  ```
  cd dexcomfollow
  ```
  ```
  pip install -r requirements.txt
  ```
  
  
# Logging in
For the code to function, you must type in your Dexcom credentials. Optionally, if you want to receive your data via email you will need to prompt in your email credentials inside dedicated variables. You can do it all by editing mydata.py variables or by entering data when running mydata.py. By default code works only with gmail accounts. If you wish to change service provider go to # https://www.systoolsgroup.com/imap/ and change ```gmail_host```(line 116) value to your chosen one.

# Usage 
There are 2 modes you can choose from:
![Screenshot 2022-04-20 154224](https://user-images.githubusercontent.com/72869230/164232805-6f5cacfa-3fc5-45c3-b609-2773194b6c24.png)


- **Mode [1] Live Glucose.**: Shows CGM data from the latest scan. You can set high and low glucose alerts by setting the dedicated variables to the number you want (high_glucose = 10)(low_glucose = 5), and if your sugar levels are going to exceed these boundaries you will hear a beep. You can remove the alerts by setting the sounds value to false (sounds = False).

  ![Screenshot 2022-04-16 140313](https://user-images.githubusercontent.com/72869230/163672561-9c9b7a5a-f4f3-41d1-abcf-8cef3a010b82.png)



- **Mode [2] Subscribe to the latest data with your email**: If you want to subscribe with your or any other email and receive the latest glucose readings via email, please enter all the emails within the mails.txt box. Then run the script and choose the second option. Note: In order to send emails you must allow less secure apps to access your gmail account. I would recommend creating a new a new one. Here is an article explaining how to do it! https://devanswers.co/allow-less-secure-apps-access-gmail-account/

  ![Screenshot 2022-04-16 135901](https://user-images.githubusercontent.com/72869230/163672510-b4ee7990-f23b-4f33-9c52-bb37f307d305.png)
# Settings
  ## Units (mmol/L by default)
  **mmol/L**
  ```
  mg_dl = False
  ```
  **mg/dL**
  ```
  mg_dl = True
  ```
  *Line 38*
  ## Setting alerts:
  **The script is going to play an alert sound if blood sugar levels are going to reach or go above this level (in this example 10 mmol/L)**
  ```
  high_glucose = 10 | high_glucose = 180 (if using mg/dl)            
  ```
  *Line 24*
  
  **The script is going to play an alert sound if blood sugar levels are going to go be equal or below this level (in this example 4 mmol/L)**
  ```
  low_glucose = 4
  ```
  *Line 26* 
  
  **By setting this option to True, you are going to receive alerts if your blood sugar levels are going to exceed the set range**
  ```
  sounds = True
  ```
  **By setting this option to False, you are not going to receive any alerts**
  ```
  sounds = False
  ```
  *Line 29* 
  
  ## Receiving emails
  **This variable will determine how often will you receive emails. (In this ex. every 5 minutes)**
  ```
  send_email_every_x_minutes = 5
  ```
  *Line 36* 
  
  **NOTE**: value cannot be lower then 5, bacause dexcom updates every 5 minutes.
  
  **If True, you will receive emails only if your sugar levels are going to be out of range**
  ```
  glucose_out_of_range = True
  ```
  **If False, you are going to recieve emails every time send_email_every_x_minutes expires**
  ```
  glucose_out_of_range = False
  ```
  *Line 32*
  
  ## Important information
  **Be aware, that if your blood sugar levels are unchanged, you are not going to recieve an email!**
  
  
# Start
  ```
  python mydata.py
  ```
 
# Acknowledgment
 Credits to gegebenne for developing the pydexcom API. https://github.com/gagebenne/pydexcom
