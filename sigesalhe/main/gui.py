#!/usr/bin/python
# -*- coding: latin-1 -*-

'''
Created on Feb 24, 2018

@author: Jesús Molina
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
        self.__clear = lambda: os.system('cls') #lambda function to clear screen in Windows.
        
        self.__mainMenu = ['1. Administrar Base de Datos. \n',
                           '2. Alquileres.']
        self.__dbAdminMenu = ['1. Mostrar datos de los clientes.']
        self.__tableMenu = []
        self.__endTableOptions = ['1. Modificar una fila.',
                                '2. Añadir una fila.',
                                '3. Eliminar una fila.',
                                '4. Salir de la tabla,' ]
    
    
    def getMainMenu(self):
        return self.__mainMenu
    
    
    def getDBAdminMenu(self):
        return self.__dbAdminMenu
    
    
    def getTableMenu(self):
        return self.__tableMenu
    
    
    def getEndTableOptions(self):
        return self.__endTableOptions
    
        
    def printMenu(self, menu):
        '''
        Prints out a menu.
        
        Pre: Takes a list representing a menu.
        '''
        for __x in menu:
            print __x
    
    
    def captureInput(self, menu):
        '''
        Waits for the user's input and returns it.
        
        Pre: Takes one of the menus of the class.
        
        Pos: Returns the selection as an integer.
        '''
        __selection = raw_input('¿Qué opción eliges: ')
        if __selection.isdigit() and __selection < len(menu):
            return int(__selection)
        
        
    def printFrame(self,lstToPrint):
        '''
        to-do
        '''
        for __x in lstToPrint:
            print '\n'
            __row = __x.split(' NextCamp ')
            for __y in __row:
                sys.stdout.write(' ' + __y + ' ')
        print ''
         
    def clearScreen(self):
        '''
        Clears the terminal.
        '''
        self.__clear() #Windows
        print(chr(27) + "[2J") #Linux