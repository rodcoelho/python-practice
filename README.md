## Python Projects

#### 1. Air Quality Text Alerts

Air Quality Indicator text message system - meant to be run in conjunction with chronjob. 

Run in the Command Line by employing the typical sys.argv argument: 

`$ python AirQualityNotification.py [zipcode] [phone #] [phoneprovider]` 

Command Line Argument should look something like this:

`$ python AirQualityNofication.py 94127 5550001111 T-Mobile`

Phone number should be 10 digits, not including 1 at the beginning, ex: 5550001111. 

Phone provider can be one of the following: ATT, T-Mobile, Verizon, Sprint, or metroPCS. 

You need sendmessages.py to run this. 

---

#### 2. SendMessages

.py file used in Air Quality project to send messages

To send text messages, import: `from sendmessages import sendtext` and call: `sendtext(phone number, phone provider, subject, message)`. 

Phone provider can be one of the following: ATT, T-Mobile, Verizon, Sprint, or metroPCS

To send emails, import : `from sendmessages import sendemail` and call: `sendemail(email,subject, message)`

---

#### 3. Rock Paper Scissors Game

A simple Rock-Paper-Scissors game (human vs pc) with ability to keep score.

Run `rockpaperscissors.py` to get started

This pop-up will appear within the Terminal. Use Up/Down/Enter to navigate:

![alt text](https://cloud.githubusercontent.com/assets/15854694/26028731/f4a5cf98-37eb-11e7-9bac-da3511542175.png)

If you choose yes, user will be given a choice:

![alt text](https://cloud.githubusercontent.com/assets/15854694/26028732/f6244d5e-37eb-11e7-8dbc-97861dd90b33.png)

And a screenshot from playing a few games:

![alt text](https://cloud.githubusercontent.com/assets/15854694/26028734/f7df707e-37eb-11e7-95ab-f88194807a13.png)

###### Expected Update: Next version will allow for Human1 vs. Human2 ( and PC1 vs. PC2 ) 

---

#### 4. Weather Tracker

_In production... Extract weather data from openweathermap. 
Show hour summary, 4 hour summary, and 8 hour summary of max and min temps._

Run `WeatherInd.py` and type desired zipcode

_Screenshots coming soon_

---

#### 5. Inspirational Alarm

Daily alarm randomly opens an 'inspirational' video from a list of urls on user's primary browser.  

Run `InspirationalAlarm.py`

_Screenshots coming soon_

###### Expected Update: Next version will ask user to insert preferred alarm time and ask users to input videos.




