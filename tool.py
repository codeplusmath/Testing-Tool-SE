#!/usr/bin/python
import unittest
import os
from main import *

def create_test_form():
    test = ScholarshipForm()
    test.insert_personaldetails('X Y Z', 'xyz@gmail.com', 9988776655, '123, Shivajinagar, Pune', '01-01-2000')
    test.insert_academicdetails('College of Engineering Pune', 'Computer Engineering', 'TY', 8.8)
    test.insert_familydetails(5, 'Y W Z', 'Farmer', '12th', 'A Y Z', 'Housewife', '12th', 500000)

    return test

class ScholarshipFormTests(unittest.TestCase):
    def test_personal(self):
        test = ScholarshipForm()
        test.insert_personaldetails('X Y Z', 'xyz@gmail.com', 9988776655, '123, Shivajinagar, Pune', '01-01-2000')

        self.assertTrue(type(test.name) is str)
        self.assertTrue(type(test.email) is str)
        self.assertTrue(len(str(test.phoneno)) == 10 and type(test.phoneno) is int)
        self.assertTrue(type(test.address) is str)
        self.assertEqual(len(test.DOB), 10)

    def test_academic(self):
        test = ScholarshipForm()
        test.insert_academicdetails('College of Engineering Pune', 'Computer Engineering', 'TY', 8.8)
        self.assertTrue(type(test.collegename) is str)
        self.assertTrue(type(test.branch) is str)
        self.assertTrue(type(test.currentyear) is str)
        self.assertTrue(type(test.cgpa) is float)

    def test_family(self):
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
   
   
    def test_filedata(self):
        test = create_test_form()
        test.savetofile()
        path = f'./db/{test.name}.dat'
        self.assertTrue(os.path.exists(path))


if __name__ == '__main__':
    unittest.main()

