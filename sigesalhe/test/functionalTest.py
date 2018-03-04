#!/usr/bin/python
# -*- coding: latin-1 -*-

'''
Created on Feb 24, 2018

@author: Jesús
'''

from main.client import Client
from main.dataBase import DataBase
from main.gui import GUI


if __name__ == '__main__':
    
        instGUI = GUI()
        instClient = Client()
        instDataBase = DataBase()
        
        #A employee runs the program and the Main Menu appears waiting for an input.
        instGUI.printMenu(instGUI.mainMenu)
        
        #He chooses the first option.
        instGUI.captureInput(instGUI.mainMenu)
        
        #A new menu appears.
        instGUI.clearScreen()
        instGUI.printMenu(instGUI.dbAdminMenu)
        
        #He chooses the first option again.
        instGUI.captureInput(instGUI.mainMenu)
        
        #A formatted list of all the clients shows up. At the end of the screen
        #more options appears and the program waits for an input.
        listClients = instDataBase.showClientTable()
        instGUI.printFrame(listClients)
        instGUI.printMenu(instGUI.endTableOptions)
        instGUI.captureInput(instGUI.endTableOptions)
        
        #The user selects the option '1. Modificar una fila'. 
        