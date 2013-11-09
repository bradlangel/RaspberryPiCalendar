'''
Created on Nov 6, 2013

@author: bradlangel
'''
import httplib2
import os

import json

from apiclient.discovery import build
from oauth2client import file
from oauth2client import client
from oauth2client import tools
from calendarIDs import *
from Event import *
from dateTime import *


class CalendarRepository():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''      
        
        # CLIENT_SECRETS is name of a file containing the OAuth 2.0 information for this
        # application, including client_id and client_secret. You can see the Client ID
        # and Client secret on the APIs page in the Cloud Console:
        # <https://cloud.google.com/console#/project/33218366799/apiui>
        CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), 'client_secrets.json')
    
        # Set up a Flow object to be used for authentication.
        # Add one or more of the following scopes. PLEASE ONLY ADD THE SCOPES YOU
        # NEED. For more information on using scopes please see
        # <https://developers.google.com/+/best-practices>.
        FLOW = client.flow_from_clientsecrets(CLIENT_SECRETS,
            scope=[
                'https://www.googleapis.com/auth/calendar',
                'https://www.googleapis.com/auth/calendar.readonly',
                ],
                message=tools.message_if_missing(CLIENT_SECRETS))
            
        # If the credentials don't exist or are invalid run through the native client
        # flow. The Storage object will ensure that if successful the good
        # credentials will get written back to the file.
        storage = file.Storage('sample.dat')
        credentials = storage.get()
            
        # Create an httplib2.Http object to handle our HTTP requests and authorize it
        # with our good Credentials.
        http = httplib2.Http()
        http = credentials.authorize(http)
            
        # Construct the service object for the interacting with the Calendar API.
        service = build('calendar', 'v3', http=http)

        
        
        self.FLOW = FLOW
        self.service = service
        
    def GetEvents(self, today, calId):
        
        events = list()
        
        #page token to go through all events
        page_token = None
                
        while True:
            # Construct the collection of events
            collection = self.service.events()
            # Construct a request for list of product and design events
            request = collection.list(calendarId=calId, pageToken = page_token)
            # Grab the response from the product calendar
            response = request.execute()
                
                #Parse Json data
            if 'items' in response: 
                for event in response['items']:
                    if 'start' in event:
                        if 'dateTime' in event['start']:
                            eventStart = dateTime(event['start']['dateTime'])                            
                            if today in eventStart.Date:
                                eventEnd = dateTime(event['end']['dateTime'])
                                events.append(Event(event['summary'], 
                                                    eventStart.Date, 
                                                    eventStart.Time, 
                                                    eventEnd.Date, 
                                                    eventEnd.Time))
            page_token = response.get('nextPageToken')
            if not page_token:
               break                    
        
        return events                    
                       

                                
        
        
        
                