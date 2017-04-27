Last login: Wed Apr 26 10:32:17 on ttys000
rcoelho-MBP:~ rcoelho$ python
Python 2.7.13 |Anaconda custom (x86_64)| (default, Dec 20 2016, 23:05:08) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
Anaconda is brought to you by Continuum Analytics.
Please check out: http://continuum.io/thanks and https://anaconda.org
>>> import schedule
>>> import time
>>> import webbrowser
>>> import random
>>> link1 = “https://www.youtube.com/watch?v=hER0Qp6QJNU&feature=youtu.be:
  File "<stdin>", line 1
    link1 = “https://www.youtube.com/watch?v=hER0Qp6QJNU&feature=youtu.be:
            ^
SyntaxError: invalid syntax
>>> link1 = “https://www.youtube.com/watch?v=hER0Qp6QJNU&feature=youtu.be:"
  File "<stdin>", line 1
    link1 = “https://www.youtube.com/watch?v=hER0Qp6QJNU&feature=youtu.be:"
            ^
SyntaxError: invalid syntax
>>> link1 = "https://www.youtube.com/watch?v=hER0Qp6QJNU&feature=youtu.be:"
>>> link1 = "https://www.youtube.com/watch?v=YTuElM6T50w"
>>> link1 = "https://www.youtube.com/watch?v=hER0Qp6QJNU&feature=youtu.be:"
>>> link2 = "https://www.youtube.com/watch?v=YTuElM6T50w"
>>> link3 = "https://www.youtube.com/watch?v=Sm95eZ1PZL0"
>>> link4 = "https://www.youtube.com/watch?v=CdUCndZfEzQ"
>>> link5 = "https://www.youtube.com/watch?v=e8jIZ3NB7s4"
>>> link6 = "https://www.youtube.com/watch?v=gc0x5e3MDoE"
>>> foo = [link1, link2, link3, link4, link5, link6]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def openlink():
...     webbrowser.open(random.choice(foo))
... 
>>> schedule.every(1).minutes.do(openlink)
Every 1 minute do openlink() (last run: [never], next run: 2017-04-26 10:39:52)
>>> 
>>> while True:
...     schedule.run_pending()
...     time.sleep(1)
... 
^CTraceback (most recent call last):
  File "<stdin>", line 3, in <module>
KeyboardInterrupt
>>> schedule.every().day.at("8:15").do(openlink)
Every 1 day at 08:15:00 do openlink() (last run: [never], next run: 2017-04-27 08:15:00)
>>> while True:
...     schedule.run_pending()
...     time.sleep(1)
... 
^CTraceback (most recent call last):
  File "<stdin>", line 3, in <module>
KeyboardInterrupt
>>> 
