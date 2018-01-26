#@Author Prathamesh More

import time
import calendar

tick = time.time()

print(tick)

localTime = time.asctime(time.localtime(time.time()))

print(localTime)


month = calendar.month(2018,2)

print(month)


#Check whetever leap year or not
leap = calendar.isleap(2018)

print(leap)