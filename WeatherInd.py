import time, json, urllib2
from datetime import datetime

#asks user what zipcode they would like to track weather data from

#variables to define how often data is collected, and for how many times
quarterinterval = 900 #15mins = 900seconds
numberoftimes = 96 #4 per hour * 24 hours = 96 15min segments/day

#lists to store data (quarter = 15mins, hour = 60mins, four = 4hours, day = 16hours)
quarterList = []
maxHour = []
minHour = []
maxFour = []
minFour = []
maxDay = []
minDay = []

def main():
    #C is a variable, we use this to store the most recent temperature
    zipcode = raw_input("Type zipcode and press enter: ")
    url = "http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=caacba9adefeac8c8af17749e5f73d6c" % zipcode

    C, weatherinfo = LoadCurrentTemp()

    # tells user the city, the initial temp, date and time
    print "City: ", weatherinfo["name"]
    print "Initial Temp: ", C
    print "Time: ", datetime.now().strftime('%H:%M:%S')
    print "Date: ", datetime.now().strftime('%m-%d-%Y')

    def quartercollect(): # function that collects data each 15 mins
        def quartercollect_list(): # function adds C to end of list. If any list length == 4, it 'empties' the list.
            quarterList.append(C)
            if len(maxFour) == 4 and len(minFour) == 4:
                maxDayVar = max(maxFour)
                maxDay.append(maxDayVar)
                minDayVar = min(minFour)
                minDay.append(minDayVar)
                print_summary()
                quit()

            if len(maxHour) == 4 and len(minHour) == 4:
                maxFourVar = max(maxHour)
                maxFour.append(maxFourVar)
                resetMaxHour()
                minFourVar = min(maxHour)
                minFour.append(minFourVar)
                resetMinHour()

            if len(quarterList) == 4:
                maxHvar = max(quarterList)
                maxHour.append(maxHvar)
                minHvar = min(quarterList)
                minHour.append(minHvar)
                resetQList()

        quartercollect_list()
        time.sleep(quarterinterval)  # sleeps for interval (15mins)

    # Stores C with most recent temp, calls function to store data, prints data
    for i in range (0, numberoftimes):
        LoadCurrentTemp()
        quartercollect()
        print_summary()

def print_summary():
    print "Recent Temp of Last Hour", quarterList
    print "Min Temp of Last 4 Hours", minHour
    print "Min Temp of Last 16 Hours", minFour
    print "Max Temp of Last 4 Hours", maxHour
    print "Max Temp of Last 16 Hours", maxFour

# pulls data from URL
def LoadCurrentTemp():
    weatherbot = urllib2.urlopen(url)
    weatherinfo = json.load(weatherbot)
    C = weatherinfo["main"]["temp"] / 10
    return C, weatherinfo

# resets list
def resetQList():
    quarterList = []
    return quarterList
def resetMaxHour():
    maxHour = []
    return maxHour
def resetMinHour():
    minHour = []
    return minHour

if __name__ == "__main__":
    main()

##once you want to add text messages:
##import yagmail
##configure message with appropriate variables, then send to the email with the following info:
##Just substitute a 10-digit cell number for 'number'(AT&T):   number@txt.att.net

