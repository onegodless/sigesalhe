#!/usr/bin/python
# -*- coding: latin-1 -*-

'''
Created on Feb 24, 2018

@author: Jesús
'''

import os
import sys


class GUI(object):
    '''
    classdocs
    '''

    def __init__(self):
        
        '''
        Constructor
        '''
        self.clear = lambda: os.system('cls') #lambda function to clear screen.
        
        self.mainMenu = ['1. Administrar Base de Datos. \n',
                         '2. Alquileres.']
        self.dbAdminMenu = ['1. Mostrar datos de los clientes.']
        self.tableMenu = []
        self.endTableOptions = ['1. Modificar una fila.',
                                '2. Añadir una fila.',
                                '3. Eliminar una fila.',
                                '4. Salir de la tabla,' ]
        
        
    def printMenu(self, menu):
        
        for x in menu:
            print x
    
    
    def captureInput(self, menu):
        
        selection = raw_input('¿Qué opción eliges: ')
        if selection.isdigit() and selection < len(menu):
            return int(selection)
        
        
    def printFrame(self,lstToPrint):
        for x in lstToPrint:
            print '\n'
            row = x.split(' NextCamp ')
            for y in row:
                sys.stdout.write(' ' + y + ' ')
        print ''
         
    def clearScreen(self):
           
        self.clear() #Windows
        print(chr(27) + "[2J") #Linux