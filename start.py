'''
Created on Nov 7, 2013

@author: bradlangel
'''
from calendarrepository import *

calendarRepo = CalendarRepository().GetEvents("2013-11-08", product)        
print calendarRepo[0].summary
print calendarRepo[1].summary