'''
Created on Nov 7, 2013

@author: bradlangel
'''
from calendarrepository import *
import datetime


calendarRepo = CalendarRepository().GetEvents(unicode(datetime.date.today()), product)        

print len(calendarRepo)
if len(calendarRepo):
    print calendarRepo[0].summary
    print calendarRepo[1].summary
    
