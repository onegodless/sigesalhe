#!/usr/bin/python
# -*- coding:latin-1 -*-


'''
Created on Feb 23, 2018

@author: Jes�s
'''

class Client(object):
    '''
    classdocs
    '''


    def __init__(self, dni='00000000X', name='John', lstName='Doe', tlf='000000000', address=''):
        '''
        Constructor
        '''
        
        self.dni = dni
        self.name = name
        self.lstName = lstName
        self.tlf = tlf
        self.address = address
        
        
    def __insertValues(self):
        pass
    
    
    def valideteValues(self):
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
                    print 'El �ltimo caracter del campo DNI debe ser una letra.'
            else:
                print 'los 8 primeros caracteres del campo DNI deben ser n�meros.'
        else:
            print 'El campo DNI tiene 9 caracteres'       
        #####name validation#####
        if len(self.name) < 21:
            if self.name.isalpha:
                lstReturnValues[1] = self.name
            else:
                print 'Has introducido valores no alfab�ticos en el campo nombre.'
        else:
            print 'Demasiados caracteres en el campo nombre.'
        
        #####last name validation######
        if len(self.lstName) < 21:
            if self.lstName.isalpha:
                lstReturnValues[2] = self.lstName
            else:
                print 'Has introducido caracteres no alfab�ticos en el campo apellido.'
        else:
            print 'El campo apellido debe tener 20 caracteres como m�ximo.'
        
        #####tlf validation####
        if len(self.tlf) == 9:
            if self.tlf.isdigit():
                lstReturnValues[3] = self.tlf
            else:
                print 'El campo tlf s�lo puede contener n�meros.'
        else:
            print 'El campo tlf debe tener 9 caracteres.'
            
        #####address validation#####
        if len(self.address) < 101:
            lstReturnValues[4] = self.address
        else:
            print 'El campo direcci�n debe tener 80 caracteres como m�ximo.'
            
        return lstReturnValues
