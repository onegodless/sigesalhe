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
        
        self.__dni = dni
        self.__name = name
        self.__lstName = lstName
        self.__tlf = tlf
        self.__address = address
        
        self.__instRandom = Random()
        self.__instFaker = Faker()
        
        self.validateValues()
        
        
    def __str__(self):
        
        return 'DNI: %s.\nNombre: %s.\nApellido: %s.\nTeléfono: %s.\n' \
        'Dirección: %s' % (self.__dni, self.__name, self.__lstName, self.__tlf, self.__address) 
        
        
            
    def inputClient(self):
        '''
        Ask the user to introduce the data for a client.
        
        Pre: 
        
        Pos: assigns the data that the user introduced into the instance properties, calls
        validateValues() to validate the data and then returns the list.
        '''
        self.__dni = raw_input('Inserta el DNI del cliente. 8 números más una letra sin espacios ni símbolos: ') #to-do: reject any DNI already in the DB.
        self.__name = raw_input('Inserta el Nombre del cliente. 20 caracteres alfabéticos como máximo: ')
        self.__lstName = raw_input('Inserta el Apellido del cliente. 20 caracteres alfabéticos como máximo: ')
        self.__tlf = raw_input('Inserta el Teléfono del cliente. 9 números: ')
        self.__address = raw_input('Inserta el Domicilio del cliente. 100 caracteres como máximo: ')
        
        __validatedClient = self.validateValues()
        return __validatedClient
    
    
    def validateValues(self):
        '''
            Validates the client's data before it's inserted into the table.
            
            Pre: uses the attributes of the class concerning the client's data.
            
            Pos: returns the validated data of the client.
        '''
        
        ######dni validation#####
        __lstReturnValues = ['','','','',''] #dni, name, lname, tlf, address

        __dniNumbers = self.__dni[0:8] #slice the numbers of the id.
        __dniLetter = self.__dni[-1] #slice the letter of the id.
                
        if len(self.__dni) == 9: #9 characters max.
            if __dniNumbers.isdigit():
                if __dniLetter.isalpha():
                    __lstReturnValues[0] = self.__dni
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
        if len(self.__name) < 21:
            if self.__name.isalpha:
                __lstReturnValues[1] = self.__name
            else:
                print 'Has introducido valores no alfabéticos en el campo nombre.'
                return'error'
        else:
            print 'Demasiados caracteres en el campo nombre.'
            return 'error'
        
        #####last name validation######
        if len(self.__lstName) < 21:
            if self.__lstName.isalpha:
                __lstReturnValues[2] = self.__lstName
            else:
                print 'Has introducido caracteres no alfabéticos en el campo apellido.'
                return 'error'
        else:
            print 'El campo apellido debe tener 20 caracteres como máximo.'
            return 'error'
        
        #####tlf validation####
        if len(self.__tlf) == 9:
            if self.__tlf.isdigit():
                __lstReturnValues[3] = self.__tlf
            else:
                print 'El campo tlf sólo puede contener números.'
                return'error'
        else:
            print 'El campo tlf debe tener 9 caracteres.'
            return 'error'
            
        #####address validation#####
        if len(self.__address) < 101:
            __lstReturnValues[4] = self.__address
        else:
            print 'El campo dirección debe tener 80 caracteres como máximo.'
            return 'error'
            
        return __lstReturnValues
    
    
    def generateClients(self):
        '''
        Generates all the data for a client with random values.
        
        Pre: Validates the generated data with the validateValues() method.
        
        Pos: Returns a list of strings with all the random data for a fictional client.
        '''
        __fakeDNI = str(self.__instRandom.randrange(45000000, 45999999))+self.__instFaker.random_letter()
        __fakeName =  str(self.__instFaker.first_name()) 
        __fakelName = str(self.__instFaker.last_name())
        __fakeTlf = str(self.__instRandom.randrange(100000000, 999999999))
        __fakeAdress = str(self.__instFaker.street_address())
        
        self.__dni = __fakeDNI
        self.__name = __fakeName
        self.__lstName = __fakelName
        self.__tlf = __fakeTlf
        self.__address = __fakeAdress
        
        
        __lstRandomClient = self.validateValues()
        return __lstRandomClient

    