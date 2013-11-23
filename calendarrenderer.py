'''
Created on Nov 11, 2013

@author: bradlangel
'''

from PIL import Image, ImageTk
from renderer import *
from point import *

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, numberOfRows, tileColor = '#ffffff', textColor = '#000000', summaryColor = '#000000'):
        '''
        Constructor
        '''
        Renderer.__init__(self)
        self.tileColor = tileColor
        self.textColor = textColor
        self.summaryColor = summaryColor
        self.numberOfRows = numberOfRows
        
        
    def CalculatePostBounds(self):
        self.screenWidth = self.root.winfo_screenwidth() *.5
        self.screenHeight = self.root.winfo_screenheight()

        self.eventSpacing = 10
        totalWidthOfSpacingBetweenEvents = self.eventSpacing
        totalHeightOfSpacingBetweenEvents = self.numberOfRows * self.eventSpacing
    
        self.eventWidth = (self.screenWidth - totalWidthOfSpacingBetweenEvents)
        self.eventHeight = (self.screenHeight - totalHeightOfSpacingBetweenEvents) / self.numberOfRows    
    
    def DrawCalendar(self, calendar):
        point = Point(0, 0)
        self.colorIndex = 0

        for index, event in enumerate(calendar):
            self.DrawEvent(event, point.x, point.y, self.eventWidth, self.eventHeight)
            point = self.MovePoint(point)
        
        
    def DrawEvent(self, event, x, y, width, height):
        self.RotateTileColor()
        
        self.DrawTile((x, y, x + width, y + height))
        self.DrawSummary(event.summary + ":  " + event.description, x + self.eventSpacing, (y + self.eventHeight) - (3.5 * self.eventSpacing), width - (3 * self.eventSpacing))
        ##self.DrawDescription(event.description, x + self.eventSpacing, (y + self.eventHeight) - (3.5 * self.eventSpacing), width - (3 * self.eventSpacing))
        self.DrawText(event.startTime + " -- " + event.endTime + " EndDate:" + event.endDate, x + self.eventSpacing, y + self.eventSpacing, width - (3 * self.eventSpacing))
        
    def MovePoint(self, point):
        point.x += self.eventWidth + self.eventSpacing

        if point.x > self.screenWidth:
            point.x = 0
            point.y += self.eventHeight + self.eventSpacing
        
        return point
    
    
    def DetermineTileColor(self, calendarType):
        colors = ['product', 'webDev', 'mktg', 'sales', 'core', 'afterevents']
        colors.append([])
        colors.ind
        
        
        
    
    
    
    def DrawTile(self, bounds):
        self.canvas.create_rectangle(
            bounds,
            fill = self.tileColor)
        
    def DrawText(self, text, x, y, width):
        self.canvas.create_text(
            x, y,
            anchor = 'nw',
            fill = self.textColor,
            font = ('Cambria', 20),
            text = text,            
            width = width)
        
    def DrawSummary(self, summary, x, y, width):
        self.canvas.create_text(
            x, y,
            anchor = 'nw',
            fill = self.summaryColor,
            font = ('Courier', 20),
            text = summary,            
            width = width)
        
    def DrawDescription(self, description, x, y, width):
        self.canvas.create_text(
            x, y,
            anchor = 'nw',
            fill = self.summaryColor,
            font = ('Courier', 20),
            text = description,            
            width = width)                 