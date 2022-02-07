'''
Artifact refinement for CS499

Created on Jan 21, 2022

@author: Spencer Hayden
'''

from datetime import datetime


class AppointmentService:
    '''
    classdocs
    '''
    #Creates Appointment list array
    Appointments = []
    
    #Function to add appointment object to list array
    def add_appointment(self, appointment):
        
        validateAppoinment = False
        
        for obj in AppointmentService.Appointments:
            if obj.equals(appointment):
                validateAppoinment = True
                
        if not validateAppoinment:
            AppointmentService.Appointments.append(appointment)
            return True
            
        else :
                return False
     
    #Function to update appointment object in array list        
    def update(self, appt_id, date, description):
        for obj in AppointmentService.Appointments:
            if obj.get_id() == appt_id:
                
                if date is not None and date < (datetime.now()) and obj.get_date() != date:  
                    obj.set_date(date)
                
                if description is not None and len(description) <= 50 and obj.get_description() != description:
                    obj.set_description(description)
                
                return True
        
        return False
    
    #Function to delete appoinment object from array list
    def delete_appointment(self, appt_id):
        for obj in AppointmentService.Appointments:
            
            if obj.get_id() == appt_id:
                AppointmentService.Appointments.remove(obj)
                
                return True
        
        return False
        
    
    