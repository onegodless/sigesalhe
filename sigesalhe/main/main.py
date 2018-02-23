#! /usr/bin/python
# -*- coding: latin-1 -*-


from client import Client
from dataBase import DataBase

'''
Created on Feb 23, 2018

@author: Jesús
'''


if __name__ == '__main__':
    
    instDataBase = DataBase()
    instClient = Client()
    '''
    lstRandomClient = instClient.generateClients()
    instDataBase.insertClient(lstRandomClient)
    '''
    #instDataBase.findRow()
    clientRow = instClient.inputClient()
    instDataBase.insertClient(clientRow)
    
    
    
    