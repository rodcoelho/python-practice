import json, sys
import urllib.request as urllib3
from sendmessages import sendtext
url = "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=%s&distance=50&API_KEY=2B8FF698-90F3-4000-B2D5-4089A2D6B03C" %sys.argv[1]
### this should be run completely in the Command Line by employing the typical sys.argv argument
# example:  $ python AQI1.py zipcode phone_number phone_provider
# sys.argv[0] = AQI1.py
# sys.argv[1] = zipcode
# sys.argv[2] = phone number (10 digits, not including 1 at the beginning, ex: 5550001111)
# sys.argv[3] = phone provider ('ATT', 'T-Mobile', 'Verizon', 'Sprint', 'metroPCS')

def begin():
    print(len(sys.argv))
    if (len(sys.argv) == 4):
        provider, phone = determineTextInfo()
        TextAQILoop(phone=phone, provider=provider)
    elif (len(sys.argv) == 2):
        storeTxtFile()
    else:
        print("boo!")

#Determines phone number email information
def determineTextInfo():
    phone = sys.argv[2]
    x = sys.argv[3]
    return x, phone

#extracts the AQI from AirNowAPI.org
def extractAQI():
    weatherbot = urllib3.urlopen(url)
    weatherinfo = json.load(weatherbot)
    currentWeather = int(weatherinfo[1]["AQI"])
    return currentWeather, weatherinfo

#While loop that checks AQI every hour, appropriate text message
def TextAQILoop(phone, provider):
    currentWeather, weatherInfo = extractAQI()
    msgSAFE = " Today, the Air Quality Index is %s. The levels ARE safe. Stay healthy " % currentWeather
    msgMODERATE = " Today, the Air Quality Index is %s. The pollution levels are moderate, it is NOT safe for strenuous activities " % currentWeather
    msgUNSAFE = " Today, the Air Quality Index is %s. The pollution levels ARE high " % currentWeather
    if currentWeather > 50:
        sendtext(phone, provider, "AQI Alert: HIGH", msgUNSAFE)
    elif 35 < currentWeather < 49:
        sendtext(phone, provider, "AQI Alert: MODERATE", msgMODERATE)
    else:
        sendtext(phone, provider, "AQI Alert: SAFE", msgSAFE)

def storeTxtFile():
    currentWeather, weatherInfo = extractAQI()
    msgSAFE = " Today, the Air Quality Index is %s. The levels ARE safe. Stay healthy " % currentWeather
    msgMODERATE = " Today, the Air Quality Index is %s. The pollution levels are moderate, it is NOT safe for strenuous activities " % currentWeather
    msgUNSAFE = " Today, th Air Quality Index is %s. The pollution levels ARE high " % currentWeather
    print("Will now write to file.")
    file = open("/tmp/msg.txt", 'w')
    if currentWeather > 50:
        file.write( "AQI Alert: HIGH" )
        file.write(msgUNSAFE)
        file.close()
    elif 35 < currentWeather < 49:
        file.write("AQI Alert: MODERATE")
        file.write(msgMODERATE)
        file.close()
    else:
        file.write("AQI Alert: SAFE")
        file.write(msgSAFE)
        file.close()

begin()