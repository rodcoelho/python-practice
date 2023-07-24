import schedule
import time
import webbrowser
import random


link1 = "https://www.youtube.com/watch?v=hER0Qp6QJNU&feature=youtu.be:"
link2 = "https://www.youtube.com/watch?v=YTuElM6T50w"
link3 = "https://www.youtube.com/watch?v=Sm95eZ1PZL0"
link4 = "https://www.youtube.com/watch?v=CdUCndZfEzQ"
link5 = "https://www.youtube.com/watch?v=e8jIZ3NB7s4"
link6 = "https://www.youtube.com/watch?v=gc0x5e3MDoE"

foo = [link1, link2, link3, link4, link5, link6]



def openlink():
     webbrowser.open(random.choice(foo))
 

schedule.every(1).minutes.do(openlink)

while True:
     schedule.run_pending()
     time.sleep(1)

 
schedule.every().day.at("8:15").do(openlink)

while True:
     schedule.run_pending()
     time.sleep(1)
