#!/usr/bin/python
# -*- coding: latin-1 -*-

'''
Created on Feb 24, 2018

@author: Jes�s
'''

from main.dataBase import DataBase

if __name__ == '__main__':
    
    instDataBase = DataBase()
    
    queryPos = instDataBase.findRow('Kyle Wright')
    instDataBase.printRow(queryPos)
    