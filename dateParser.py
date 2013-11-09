'''
Created on Nov 8, 2013

@author: bradlangel
'''

class dateParser():
    '''
    classdocs
    '''


    def __init__(self, calendarDate):
        '''
        Constructor
        '''
        self.date = calendarDate
        
    def parser(self, commonString):
        
        parsedTuple = self.date.partition(commonString)
        return parsedTuple
        