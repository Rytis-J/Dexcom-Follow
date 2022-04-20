# Dexcom-follow
Having an issue with your Dexcom Follow app? Or maybe you just want to get your Dexcom data/recieve alerts on computer?! Get your live Dexcom data via email, live in your Command Prompt!

# Setup
  If not installed, install Python 3, Git - https://www.python.org/downloads/ https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
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
In order for the code to function, you must type in your dexcom credentials. Optionaly, if you want to recieve your data via email you will need to prompt in your email credentials inside dedicated veriables. You can do it all by editing mydata.py veriables or by entering data when running mydata.py

# Usage 
There are 2 modes you can choose from:
![Screenshot 2022-04-20 154224](https://user-images.githubusercontent.com/72869230/164232805-6f5cacfa-3fc5-45c3-b609-2773194b6c24.png)


- **Mode [1] Live Glucose.**: Shows CGM data from the latest scan. You can set high and low glucose alerts by setting the dedicated variables to the number you want (high_glucose = 10)(low_glucose = 5), and if your sugar levels are going to exceed these boundaries you will hear a beep. You can remove the alerts by setting the sounds value to false (sounds = False).

  ![Screenshot 2022-04-16 140313](https://user-images.githubusercontent.com/72869230/163672561-9c9b7a5a-f4f3-41d1-abcf-8cef3a010b82.png)



- **Mode [2] Subscribe to the latest data with your email**: If you want to subscribe with your or any other email and receive the latest glucose readings, please enter all the emails within the mails.txt box. Then run the script and choose the second option. Note: In order to send emails you must allow less secure apps to access your gmail account. I would recommend creating a new a new one. Here is an article explaining how to do it! https://devanswers.co/allow-less-secure-apps-access-gmail-account/

  ![Screenshot 2022-04-16 135901](https://user-images.githubusercontent.com/72869230/163672510-b4ee7990-f23b-4f33-9c52-bb37f307d305.png)
 # Start
  ```
  python mydata.py
  ```
 
 # Credits
 Credits to gegebenne for developing pydexcom API. https://github.com/gagebenne/pydexcom
