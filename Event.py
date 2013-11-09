'''
Created on Nov 8, 2013

@author: bradlangel
'''

class Event():
    '''
    classdocs
    '''
    def __init__(self, summary, startDate, startTime, endDate, endTime):
        '''
        Constructor
        '''
        self.summary = summary
        self.startDate = startDate
        self.start = startTime
        self.end = endTime
        self.endDate = endDate