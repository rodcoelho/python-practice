import time, json, urllib2, datetime
from pick import pick
from sendmessages import sendemail, sendtext

#Questions and prompts
pop_up = "Do you want to receive a text message or email when the air quality is unsafe?"
pop_answer = ('Yes, I would like a text message', 'Yes, I would like an email in the morning', 'Neither, I will check the AQI on my own')
phone_provider = "What is your phone provider?"
decide_provider = ('ATT', 'T-Mobile', 'Verizon', 'Sprint', 'metroPCS')
zipcode = raw_input("Type zipcode and press enter: ")
url = "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=%s&distance=50&API_KEY=2B8FF698-90F3-4000-B2D5-4089A2D6B03C" %zipcode

#Asks user if he/she wants to receive text message/email when AQI level is too high
def begin():
    pop_decision = pick(pop_answer, pop_up)
    if pop_decision[1] == 0:
        provider, phone = determineTextInfo()
        TextAQILoop(phone=phone, provider=provider)
    elif pop_decision[1] == 1:
        email = determineEmailInfo()
        EmailAQILoop(email=email)
    else:
        quit()

#Allows user to input their phone number and phone provider (so we can send emails to their phone number)
def determineTextInfo():
    phone = raw_input("Type phone number (ex. type 222333444, not 222-333-444) and press enter: ")
    prov = pick(decide_provider, phone_provider)
    x = prov[0]
    return x, phone

#Allows user to input their email address
def determineEmailInfo():
    email = raw_input("Type your email address and press enter: ")
    return email

#extracts the AQI from AirNowAPI.org
def extractAQI():
    weatherbot = urllib2.urlopen(url)
    weatherinfo = json.load(weatherbot)
    currentWeather = weatherinfo[0]["AQI"]
    return currentWeather, weatherinfo

#While loop that checks AQI every hour, sends text if conditions are met
def TextAQILoop(phone, provider):
    currentWeather, weatherInfo = extractAQI()
    sendtext(phone, provider, "AQI Alert", """You will now receive Air Quality notifications. 
    If the AQI (Air Quality Index) is above 50, we will notify you. 
    Today, the AQI is %s. 
    Stay Healthy!""") % currentWeather
    x = 1
    while x == 1:
        currentWeather, weatherInfo = extractAQI()
        if currentWeather > 50:
            sendtext(phone, provider, "AQI Alert", "The Air Quality Index is %s. Exercise with Caution.") % currentWeather
            #gives user an 3 hour break so they don't receive a text message every hour (#annoying)
            time.sleep(7200)
        elif currentWeather < 1 or None:
            sendtext(phone, provider, "Error", "The website's API or json may have changed. That, or my code is broken")
        time.sleep(3600)

#For loop that emails every morning at 8am if AQI is high... does this for one year
def EmailAQILoop(email):
    currentWeather, weatherInfo = extractAQI()
    sendemail(email, "AQI Alert",
             """"You will now receive Air Quality notifications. 
             If the AQI (Air Quality Index) is above 50, we will notify you. 
             Today, the AQI is %s. 
             Stay Healthy!""") % currentWeather
    for i in xrange(0, 365):
        # sleep until 8AM
        t = datetime.datetime.today()
        future = datetime.datetime(t.year, t.month, t.day, 8, 0)
        if t.hour >= 8:
            future += datetime.timedelta(days=1)
        time.sleep((future - t).seconds)
        currentWeather, weatherInfo = extractAQI()
        if currentWeather > 50:
            sendemail(email, "AQI Alert", "The Air Quality Index is %s. Exercise with Caution.") % currentWeather
        elif currentWeather < 1 or None:
            sendemail(email, "Error", "The website's API or json may have changed. That, or my code is broken")

begin()
##Next update: create seperate .py file that stores the email address and phone number, preference for how often to run the code etc.