## Python Projects
###### Basic warm up projects


#### 1. Cracking the Coding Interview Solutions

PDF: https://inspirit.net.in/books/placements/Cracking%20the%20Coding%20Interview.pdf

Solutions in repo have been made into comments to allow for testing of individual solutions

---

#### 2. Inspirational Alarm

Daily alarm opens random 'inspirational' video from a list of urls from user's primary browser.

Run `InspirationalAlarm.py`

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


#### 4. Air Quality Text Alerts

AQI (Air Quality Index) text message system - meant to be run in conjunction with chronjob.

Run in the Command Line by employing the typical sys.argv argument:

`$ python AirQualityNotification.py [zipcode] [phone #] [phoneprovider]`

Command Line Argument should look something like this:

`$ python AirQualityNofication.py 94127 5550001111 T-Mobile`

Phone number should be 10 digits, not including 1 at the beginning, ex: 5550001111.

Phone provider can be one of the following: ATT, T-Mobile, Verizon, Sprint, or metroPCS.

You need sendmessages.py to run this (found in my repository)

---

#### 5. SendMessages

.py file used in Air Quality project to send messages

To send text messages, import: `from sendmessages import sendtext` and call: `sendtext(phone number, phone provider, subject, message)`.

Phone provider can be one of the following: ATT, T-Mobile, Verizon, Sprint, or metroPCS

To send emails, import : `from sendmessages import sendemail` and call: `sendemail(email,subject, message)`


---

#### 6. Cashier Change Converter

Function that gives the user, or Cashier, the bills and coins needed to give someone change after a cash purchase.

As an example, if the float is `112.33`, the result would be `1 $100 bill`, `1 $10 bill`, `2 $1 bills`, `1 quarter`, `1 nickel` and `3 pennies`.

---

#### 7. Weather Tracker

_In production... Extract weather data from openweathermap.
Show hour summary, 4 hour summary, and 8 hour summary of max and min temps._

Run `WeatherInd.py` with desired zipcode

_Screenshots coming soon_
