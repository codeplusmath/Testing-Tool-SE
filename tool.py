#!/usr/bin/python
import unittest
import os
from main import *

def create_test_form():
    test = ScholarshipForm()
    test.insert_personaldetails('X', 'xyz@gmail.com', 9988776655, '123, Shivajinagar, Pune', '01-01-2000')
    test.insert_academicdetails('College of Engineering Pune', 'Computer Engineering', 'TY', 8.8)
    test.insert_familydetails(5, 'Y W Z', 'Farmer', '12th', 'A Y Z', 'Housewife', '12th', 500000)
    test.savetofile()
    return test

class ScholarshipFormTests(unittest.TestCase):
    def testA_personal(self):
        print('\nTest 1: Adding Personal Details')
        test = ScholarshipForm()
        test.insert_personaldetails('X Y Z', 'xyz@gmail.com', 9988776655, '123, Shivajinagar, Pune', '01-01-2000')

        self.assertTrue(type(test.name) is str)
        self.assertTrue(type(test.email) is str)
        self.assertTrue(len(str(test.phoneno)) == 10 and type(test.phoneno) is int)
        self.assertTrue(type(test.address) is str)
        self.assertEqual(len(test.DOB), 10)

    def testB_academic(self):
        print('\nTest 2: Adding Academic Details')
        test = ScholarshipForm()
        test.insert_academicdetails('College of Engineering Pune', 'Computer Engineering', 'TY', 8.8)
        self.assertTrue(type(test.collegename) is str)
        self.assertTrue(type(test.branch) is str)
        self.assertTrue(type(test.currentyear) is str)
        self.assertTrue(type(test.cgpa) is float)

    def testC_family(self):
        print('\nTest 3: Adding Family Details')
        test = ScholarshipForm()
        test.insert_familydetails( 5, 'Y W Z', 'Farmer', '12th', 'A Y Z', 'Housewife', '12th', 500000)
        
        self.assertTrue(type(test.noofmembers) is int)
        self.assertTrue(type(test.fathername) is str)
        self.assertTrue(type(test.fatheroccupation) is str)
        self.assertTrue(type(test.fathereducation) is str)
        self.assertTrue(type(test.mothername) is str)
        self.assertTrue(type(test.motheroccupation) is str)
        self.assertTrue(type(test.mothereducation) is str)
        self.assertTrue(type(test.annualincome) is int and test.annualincome>=0)
   
   
    def testD_filedata(self):
        print('\nTest 4: Adding Form')
        test = create_test_form()
        test.savetofile()
        path = f'./db/{test.name}.dat'
        self.assertTrue(os.path.exists(path))
    
    def testE_viewdata(self):
        print('\nTest 5: View Form')
        test = create_test_form()
        
        self.assertEqual(test.viewdata(), 0)
    
    def testF_viewalldata(self):
        print('\nTest 6: View All Forms')
        test = create_test_form()
        
        self.assertEqual(test.alldata(), 0)
    
    def testG_updatedata(self):
        print('\nTest 7: Updating Form')
        test = create_test_form()
        self.assertEqual(test.updatedata(), 0)
    
    def testH_removedata(self):
        print('\nTest 8: Removing Form')
        test = create_test_form()
        
        self.assertEqual(test.removedata(), 0)
    
    def testI_viewdatanofile(self):
        print('\nTest 9: View data Form that is not present')
        test = create_test_form()
        
        self.assertEqual(test.viewdata(), 1)
            
    def testJ_updatedatanofile(self):
        print('\nTest 10: Updating Form that is not present')
        test = create_test_form()
        
        self.assertEqual(test.updatedata(), 1)
    
    def testK_removedatanofile(self):
        print('\nTest 11: Removing Form that is not present')
        test = create_test_form()
        
        self.assertEqual(test.removedata(), 1)


if __name__ == '__main__':
    unittest.main()

