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


    def viewdata(self):
        name = input("Enter name: ")
        path = f'./db/{name}.dat'
        if os.path.exists(path):
            with open(path, 'r') as f:
                print(f.read())
            print('\n')
        else:
            print('No application found')
            return 1
        return 0
        
    def removedata(self):
        name = input("Enter name: ")
        path = f'./db/{name}.dat'
        if os.path.exists(path):
            os.remove(path)
            print('Application removed successfully...\n')
        else:
            print('No application found')
            return 1
        return 0
    
    def alldata(self):
        path = f'./db/'
        for f in os.listdir(path):
            print(f)
        return 0

    def updatedata(self):
        name = input("Enter name: ")
        path = f'./db/{name}.dat'
        print('You can update one value at a time')
        param1 = input('Which data to update: ')
        value = input('Enter new data: ')
        try:
            newline = param1.split(': ')[0] + ': ' + str(value)
            reading_file = open(path, "r")
            new_file_content = ""
            for line in reading_file:
                stripped_line = line.strip()
                new_line = stripped_line.replace(param1, newline)
                new_file_content += new_line +"\n"
            reading_file.close()
            writing_file = open(path, "w")
            writing_file.write(new_file_content)
            writing_file.close()
            
        except:
            print('cannot update')
            return 1
        return 0

    def menu(self):
        print("\n\t0.Menu \n\t1.Add Form \n\t2.Show Form Data \n\t3.Show All Forms \n\t4.Remove Data \n\t5.Exit")
        while True:    
            choice = int(input("\nEnter Choice: "))
            if (choice == 0):
                self.menu()
                
            elif (choice == 1):
                print('-------Academic Details-------')
                name = input('Enter Name: ')
                email = input('Enter EmailID: ')
                phoneno = int(input('Enter Phone NO: '))
                address = input('Enter Address: ') 
                DOB = str(input('Birth Date (dd-mm-yyyy)'))
                self.insert_personaldetails(name, email, phoneno, address, DOB)
                
                print('-------Academic Details-------')
                collegename = input('Enter College Name: ')
                branch = input('Enter Branch: ')
                currentyear = input('Enter Current Year: ')
                cgpa = float(input('Enter Cgpa: '))
                self.insert_academicdetails(collegename, branch, currentyear, cgpa)
                
                print('-------Family Details-------')
                noofmembers = int(input('Enter No of family members: '))
                fathername = input('Enter Father Name:')
                fatheroccupation = input('Enter Father Occupation: ')
                fathereducation = input('Enter Father Education: ')
                mothername = input('Enter Mother Name: ')
                motheroccupation = input('Enter Mother Occupation: ')
                mothereducation = input('Enter Mother Education:')
                annualincome = int(input('Enter Annual Income: '))
                self.insert_familydetails(noofmembers, fathername, fatheroccupation, fathereducation, mothername, motheroccupation, mothereducation, annualincome)
                self.savetofile()
            
            elif (choice == 2):
                self.viewdata()
            
            elif (choice == 3):
                self.alldata()
            
            elif (choice == 4):
                self.removedata()
            
            else:
                print("\nThank You...")
                exit(0)
        return 0
        
def main():
    form = ScholarshipForm()
    form.menu()
    return 0
 
if __name__ == '__main__':
    main()