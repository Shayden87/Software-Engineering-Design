'''
Artifact refinement for CS499

Created on Jan 20, 2022

@author: Spencer Hayden
'''



class Appointment:
    
    #Initalizing object parameters
    appt_id = None
    date = None
    description = None

    #Constructor
    def __init__(self, appt_id, date, description):
        if(appt_id == None or len(appt_id) >= 10):
            raise ValueError('Invalid id')
        if(date == None or date < (date.today())):
            raise ValueError('Invalid date')
        if(description == None or len(description) > 50):
            raise ValueError('Invalid description')
        
        self.appt_id = appt_id
        self.date = date
        self.description = description
        
    #Getter and Setter for appt_id parameter
    def get_id(self):
        return self.appt_id
    
    def set_id(self, appt_id):
        self.appt_id = appt_id 
    
    #Getter and Setter for date parameter
    def get_date(self):
        return self.date
    
    def set_date(self, date):
        self.date = date
    
    #Getter and Setter for description parameter
    def  get_description(self):
        return self.description
    
    def set_description(self, description):
        self.description = description
        
    #Function to check id
    def  equals(self, obj):
        a = Appointment(obj)
        return bool(self.getId() == a.getId())
    
    #Function to return string
    def  to_string(self):
        return('Appointment ID: ' + self.get_id() + ', Date: ' + str(self.get_date()) + ', Description: ' + self.get_description() + '\n')