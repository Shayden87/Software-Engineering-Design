'''
Created on Jan 23, 2022

@author: RadicalEdward
'''
import unittest

from AppointmentService import AppointmentService
from Appointment import Appointment
from datetime import date


class Test(unittest.TestCase):

    #Test to verify adding of appointment to list
    def testAddAppointment(self):
        a = Appointment('00001', date(2022, 12, 1), 'Coffee with Brian')
        b = Appointment('00002', date(2022, 12, 3), 'Meeting with Allison')
        c = Appointment('00003', date(2022, 12, 4), 'Conference in Chicago')
        self.assertEquals(True, AppointmentService.add_appointment(a))
        self.assertEquals(True, AppointmentService.add_appointment(b)) 
        self.assertEquals(True, AppointmentService.add_appointment(c)) 
    
    #Test to verify long id length throws Value Error
    def testIdLong(self):
        with self.assertRaisesRegexp(ValueError, 'Invalid id'): 
            a = Appointment('55502100000', date(2022, 12, 1), 'Business Meeting with share holders')
            AppointmentService.add_appointment(a)
    
    #Test to verify id of None throws Value Error
    def testIdNone(self):
        with self.assertRaisesRegexp(ValueError, 'Invalid id'):
            a = Appointment(None, date(2022, 12, 1), 'Business Meeting with share holders')                                               
            AppointmentService.add_appointment(a)
    
    #Test to verify past date throws Value Error
    def testDateInPast(self):
        with self.assertRaisesRegexp(ValueError, 'Invalid date'):
            a = Appointment('55555', date(2021, 12, 1), 'Business Meeting with share holders')                                               
            AppointmentService.add_appointment(a)

    #Test to verify date of None throws Value Error 
    def testDateNone(self):
        with self.assertRaisesRegexp(ValueError, 'Invalid date'):
            a = Appointment('55555', None, 'Business Meeting with share holders')                                               
            AppointmentService.add_appointment(a)

    #Test to verify long description throws Value Error 
    def testDescriptionTooLong(self):
        with self.assertRaisesRegexp(ValueError, 'Invalid description'):
            a = Appointment('55555', date(2022, 12, 1), 'Vacation to the Carribean, then head back to New York for Board Meeting with the Partners')                                               
            AppointmentService.add_appointment(a)

    #Test to verify description of None throws Value Error 
    def testAppointmentDescriptionNull(self):
        with self.assertRaisesRegexp(ValueError, 'Invalid description'):
            a = Appointment('55555', date(2022, 12, 1), None)                                               
            AppointmentService.add_appointment(a)
            
    #Test to check update returns True
    def testUpdateAppointment(self):
        a = Appointment('00004', date(2022, 12, 5), 'Coffee with Kristen')
        b = Appointment('00005', date(2022, 12, 6), 'Coffee with Carlos')
        c = Appointment('00006', date(2022, 12, 7), 'Coffee with Dennis')
        self.assertEquals(True, AppointmentService.add_appointment(a))
        self.assertEquals(True, AppointmentService.add_appointment(b))
        self.assertEquals(True, AppointmentService.add_appointment(c))

        self.assertEquals(True, AppointmentService.update('00005', date(2022, 12, 6), 'Dinner with Tim'))
        self.assertEquals(True, AppointmentService.update('00006', date(2022, 12, 7), 'Dinner with Carla'))

    #Test to check delete returns True
    def testDeleteAppointment(self):
        a = Appointment('00007', date(2022, 12, 8), 'Meeting with Carla')
        b = Appointment('00008', date(2022, 12, 9), 'Meeting with Joe')
        c = Appointment('00009', date(2022, 12, 10), 'Meeting with Ashley')
        self.assertEqual(True, AppointmentService.add_appointment(a))
        self.assertEqual(True, AppointmentService.add_appointment(b))
        self.assertEqual(True, AppointmentService.add_appointment(c))

        self.assertEqual(True, AppointmentService.delete_appointment('00009'))
        self.assertEqual(True, AppointmentService.delete_appointment('00008'))

    #Test to verify to_string method is functioning properly
    def testToString(self):
        a = Appointment('55502', date(2022, 12, 12), 'Dinner with Margo')
        expected = 'Appointment ID: 55502, Date: 2022-12-12, Description: Dinner with Margo\n'
        self.assertEqual(expected, a.to_string())

    #Tests to verify assertNotEquals is working properly
    def equalsFalseTest1(self):
        a = Appointment('Randomly', date(2022, 12, 12), 'Dinner with Margo')
        b = Appointment()
        self.assertNotEquals(a, b)
    
       
    def equalsFalseTest2(self):
        a = Appointment('Randomly', date(2022, 12, 12), 'Dinner with Margo')
        b = Appointment('Randoml', date(2022, 12, 12), 'Dinner with Margo')
        self.assertNotEquals(a, b)
    
    #Tests to verify assertEquals is working properly
    def equalsTrueTest(self):
        a = Appointment('Randomly', date(2022, 12, 12), 'Dinner with Margo')
        b = Appointment('Randomly', date(2022, 12, 12), 'Dinner with Margo')
        self.assertEquals(a, b)
        
    def equalsFalseTest3(self):
        a = Appointment('Randomly', date(2022, 12, 12), 'Dinner with Margo')
        b = Appointment('Randomly', date(2022, 12, 13), 'Dinner with Margo')
        self.assertEquals(a, b)    

    
if __name__ == '__main__':
    unittest.main()  