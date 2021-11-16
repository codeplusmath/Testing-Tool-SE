#!/usr/bin/python
import os
import re

class ScholarshipForm():
    
    def __init__(self):
        # personal details
        self.name = None
        self.email = None
        self.phoneno = None
        self.address = None
        self.DOB = None
        
        # academic details
        self.collegename = None
        self.branch = None
        self.currentyear = None
        self.cgpa = None

        # family details
        self.noofmembers = None
        self.fathername = None
        self.fatheroccupation = None
        self.fathereducation = None
        self.mothername = None
        self.motheroccupation = None
        self.mothereducation = None
        self.annualincome = None

    def insert_personaldetails(self, name, email, phoneno, address, DOB):
        self.name = name
        if re.match("\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z",email,re.IGNORECASE):
            self.email = email
        else:
            self.email = ''
            print('Invalid email')
        
        if len(str(phoneno))==10:
            self.phoneno = phoneno
        else:
            print('Invalid Phone Number')
            self.phoneno = 0000000000
        self.address = address
        self.DOB = DOB

    def insert_academicdetails(self, collegename, branch, currentyear, cgpa):
        self.collegename = collegename
        self.branch = branch
        self.currentyear = currentyear
        self.cgpa = cgpa

    def insert_familydetails(self, noofmembers, fathername, fatheroccupation, fathereducation, mothername, motheroccupation, mothereducation, annualincome):
        self.noofmembers = noofmembers
        self.fathername = fathername
        self.fatheroccupation = fatheroccupation
        self.fathereducation = fathereducation
        self.mothername = mothername
        self.motheroccupation = motheroccupation
        self.mothereducation = mothereducation
        if(type(annualincome) == int and annualincome>0):
            self.annualincome = annualincome
        else:
            print('Invalid income')
            self.annualincome = 0

    def savetofile(self):
        path = f'./db/{self.name}.dat'
        if not os.path.exists(path):
            f = open(path, 'w')
            data = ''
            data += 'Name: ' + self.name + '\n' + 'Email: ' + self.email + '\n' + 'Phone No: ' + str(self.phoneno) + '\n' + 'Address: ' + self.address + '\n' + 'DOB: ' + self.DOB + '\n\n'
            data += 'College Name: ' + self.collegename + '\n' + 'Branch: ' + self.branch + '\n' + 'Current Year: ' + str(self.currentyear) + '\n' + 'CGPA: ' + str(self.cgpa) + '\n\n'
            data += 'No of members: ' + str(self.noofmembers) + '\n' + 'Father Name: ' + self.fathername + '\n' + 'Father Occupation: ' + self.fatheroccupation + '\n'
            data += 'Father Education: ' + str(self.fathereducation) + '\n' + 'Mother Name: ' + self.mothername + '\n' + 'Mother Occupation: ' + self.motheroccupation + '\n'
            data += 'Mother Education: ' + str(self.fathereducation) + '\n' + 'Annual Income: ' + str(self.annualincome) + 'INR'
            f.writelines(data)
            print('Application successfully submitted')
            f.close()

        else:
            print('Application already recieved\nYou can edit application\n')


    def viewdata(self):
        path = f'./db/{self.name}.dat'
        if os.path.exits(path):
            f = open(path, 'r')
            print(f)
            print('\n')
        else:
            print('No application found')


    def updatedata(self):
        path = f'./db/{self.name}.dat'
        print('\nYou can update one value at a time')
        param1 = input('Which data to update: ')
        value = input('Enter new data: ')
        param = param1.replace(' ', '').lower()
        try:
            line = param1 + str(self.param)
            f = open(path)
            neline = param1 + str(value)
            f.replace(line, newline)
            n = open('./db/tmp', 'w')
            n.writelines(f)
            f.close()
            n.close()
            os.remove(path)
            os.rename('./db/tmp', path)
            self.param = value
            
        except:
            print('cannot update')

