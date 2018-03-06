#!/usr/bin/python
# -*- coding: latin-1 -*-

'''
Created on Feb 24, 2018

@author: Jesús Molina
'''

from main.client import Client
from main.dataBase import DataBase
from main.gui import GUI


if __name__ == '__main__':
    
        instGUI = GUI()
        instClient = Client()
        instDataBase = DataBase()
        
        while True:
            #A employee runs the program and the Main Menu appears waiting for an input.
            instGUI.printMenu(instGUI.getMainMenu())
            
            #He chooses the admin database option.
            selection = instGUI.captureInput(instGUI.getMainMenu())
            if selection == 1:
                print 'Has elegido la opción: %s' % (instGUI.getMainMenu()[selection - 1])
                break
            
        while True:
            #A new menu appears to choose a table.
            instGUI.clearScreen()
            instGUI.printMenu(instGUI.getAdminDB())
            
            #He chooses the client table.
            selection = instGUI.captureInput(instGUI.getAdminDB())
            if selection == 1:
                print 'Has elegido la opcion: %s' % (instGUI.getAdminDB()[selection - 1])
                break
        
        while True:
            #Now the user chooses to see all the entries in the client table
            instGUI.clearScreen()
            instGUI.printMenu(instGUI.getAdminClientTableMenu())
            selection = instGUI.captureInput(instGUI.getAdminClientTableMenu())
            
            if selection == 1:
                print 'Has elegido la opcion: %s' % (instGUI.getAdminClientTableMenu()[selection - 1])
                break
            
        while True:
            #A formatted list of all the clients shows up. At the end of the screen
            #more options appears and the program waits for an input.
            listClients = instDataBase.showClientTable('clientTable.txt')
            instGUI.printFrame(listClients)
            instGUI.printMenu(instGUI.getEndTableOptions())
            instGUI.captureInput(instGUI.getEndTableOptions())
            
            #The user selects the option '1. Modificar una fila'. 
        