'''
Created on Nov 8, 2013

@author: bradlangel
'''

class Event():
    '''
    classdocs
    '''
    def __init__(self, summary, description, startDate, startTime, endDate, endTime):
        '''
        Constructor
        '''
        self.summary = summary
        self.description = description
        self.startDate = startDate
        self.start = startTime
        self.end = endTime
        self.endDate = endDate