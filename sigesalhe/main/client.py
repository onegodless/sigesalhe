#!/usr/bin/python
# -*- coding:latin-1 -*-


'''
Created on Feb 23, 2018

@author: Jesús
'''

from faker import Faker
from random import Random


class Client(object):
    
    
    def __init__(self, dni='00000000X', name='John', lstName='Doe', tlf='000000000', address=''):
        
        self.dni = dni
        self.name = name
        self.lstName = lstName
        self.tlf = tlf
        self.address = address
        self.instRandom = Random()
        self.instFaker = Faker()
        
    def __insertValues(self):
        pass
    
    
    def validateValues(self):
        '''
            Validates the format and form of the data of the client.
            
            Pre: takes the data of the client.
            
            Pro: returns the data of the client.
        '''
        
        ######dni validation#####
        lstReturnValues = ['','','','',''] #dni, name, lname, tlf, address

        dniNumbers = self.dni[0:8] #slice the numbers of the id.
        dniLetter = self.dni[-1] #slice the letter of the id.
                
        if len(self.dni) == 9: #9 characters max.
            if dniNumbers.isdigit():
                if dniLetter.isalpha():
                    lstReturnValues[0] = self.dni
                else:
                    print 'El último caracter del campo DNI debe ser una letra.'
            else:
                print 'los 8 primeros caracteres del campo DNI deben ser números.'
        else:
            print 'El campo DNI tiene 9 caracteres'       
        #####name validation#####
        if len(self.name) < 21:
            if self.name.isalpha:
                lstReturnValues[1] = self.name
            else:
                print 'Has introducido valores no alfabéticos en el campo nombre.'
        else:
            print 'Demasiados caracteres en el campo nombre.'
        
        #####last name validation######
        if len(self.lstName) < 21:
            if self.lstName.isalpha:
                lstReturnValues[2] = self.lstName
            else:
                print 'Has introducido caracteres no alfabéticos en el campo apellido.'
        else:
            print 'El campo apellido debe tener 20 caracteres como máximo.'
        
        #####tlf validation####
        if len(self.tlf) == 9:
            if self.tlf.isdigit():
                lstReturnValues[3] = self.tlf
            else:
                print 'El campo tlf sólo puede contener números.'
        else:
            print 'El campo tlf debe tener 9 caracteres.'
            
        #####address validation#####
        if len(self.address) < 101:
            lstReturnValues[4] = self.address
        else:
            print 'El campo dirección debe tener 80 caracteres como máximo.'
            
        return lstReturnValues
    
    
    def generateClients(self):
        
        fakeDNI = str(self.instRandom.randrange(45000000, 45999999))+self.instFaker.random_letter()
        fakeName =  str(self.instFaker.name_male()) 
        fakelName = str(self.instFaker.last_name())
        fakeTlf = str(self.instRandom.randrange(100000000, 999999999))
        fakeAdress = str(self.instFaker.street_address())
        
        self.dni = fakeDNI
        self.name = fakeName
        self.lstName = fakelName
        self.tlf = fakeTlf
        self.address = fakeAdress
        
        lstRandomClient = self.validateValues()
        return lstRandomClient

    