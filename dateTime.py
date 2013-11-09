'''
Created on Nov 8, 2013

@author: bradlangel
'''
from dateParser import *

class dateTime():
    '''
    classdocs
    '''


    def __init__(self, startDateTime):
        '''
        Constructor
        '''
        myDateParser = dateParser(startDateTime)
        eventDateTime = myDateParser.parser("T")
        self.Date = eventDateTime[0]
        myTimeParser = dateParser(eventDateTime[2])
        self.Time = myTimeParser.parser("-")[0]
                