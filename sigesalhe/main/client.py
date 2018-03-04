#!/usr/bin/python
# -*- coding:latin-1 -*-


'''
Created on Feb 23, 2018

@author: Jesús Molina
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
        
        self.validateValues()
        
        
    def inputClient(self):
        '''
        Ask the user to introduce the data for a client.
        
        Pre: 
        
        Pos: assigns the data that the user introduced into the instance properties, calls
        validateValues() to validate the data and then returns the list.
        '''
        self.dni = raw_input('Inserta el DNI del cliente. 8 números más una letra sin espacios ni símbolos: ') #to-do: reject any DNI already in the DB.
        self.name = raw_input('Inserta el Nombre del cliente. 20 caracteres alfabéticos como máximo: ')
        self.lstName = raw_input('Inserta el Apellido del cliente. 20 caracteres alfabéticos como máximo: ')
        self.tlf = raw_input('Inserta el Teléfono del cliente. 9 números: ')
        self.address = raw_input('Inserta el Domicilio del cliente. 100 caracteres como máximo: ')
        
        validatedClient = self.validateValues()
        return validatedClient
    
    
    def validateValues(self):
        '''
            Validates the client's data before it's inserted into the table.
            
            Pre: uses the attributes of the class concerning the client's data.
            
            Pos: returns the validated data of the client.
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
                    return 'error'
            else:
                print 'los 8 primeros caracteres del campo DNI deben ser números.'
                return 'error'
        else:
            print 'El campo DNI tiene 9 caracteres' 
            return 'error'     
        #####name validation#####
        if len(self.name) < 21:
            if self.name.isalpha:
                lstReturnValues[1] = self.name
            else:
                print 'Has introducido valores no alfabéticos en el campo nombre.'
                return'error'
        else:
            print 'Demasiados caracteres en el campo nombre.'
            return 'error'
        
        #####last name validation######
        if len(self.lstName) < 21:
            if self.lstName.isalpha:
                lstReturnValues[2] = self.lstName
            else:
                print 'Has introducido caracteres no alfabéticos en el campo apellido.'
                return 'error'
        else:
            print 'El campo apellido debe tener 20 caracteres como máximo.'
            return 'error'
        
        #####tlf validation####
        if len(self.tlf) == 9:
            if self.tlf.isdigit():
                lstReturnValues[3] = self.tlf
            else:
                print 'El campo tlf sólo puede contener números.'
                return'error'
        else:
            print 'El campo tlf debe tener 9 caracteres.'
            return 'error'
            
        #####address validation#####
        if len(self.address) < 101:
            lstReturnValues[4] = self.address
        else:
            print 'El campo dirección debe tener 80 caracteres como máximo.'
            return 'error'
            
        return lstReturnValues
    
    
    def generateClients(self):
        '''
        Generates all the data for a client with random values.
        
        Pre: Validates the generated data with the validateValues() method.
        
        Pos: Returns a list of strings with all the random data for a fictional client.
        '''
        fakeDNI = str(self.instRandom.randrange(45000000, 45999999))+self.instFaker.random_letter()
        fakeName =  str(self.instFaker.first_name()) 
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

    