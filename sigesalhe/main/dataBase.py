#!/usr/bin/python
# -*- coding: latin-1 -*-


'''
Created on Feb 23, 2018

@author: Jesús
'''


class DataBase(object):


    def __init__(self):
        pass
    
    def insertClient(self,lstValidClient):
        
        table = open('clientTable.txt', 'a')
        
        table.write(lstValidClient[0] + ' NextCamp ' + lstValidClient[1] + ' NextCamp ' + lstValidClient[2] + ' NextCamp ' + lstValidClient[3] + ' NextCamp ' + lstValidClient[4] + ' \n')
        
        table.close()  
        
        
    def findRow(self):
        
        table = open('clientTable.txt', 'r')
        
        allLines = table.readlines()
        print allLines
        for x in allLines:
            query = x.split(' ')
            for y in query:
                if y == 'Chad':
                    print query[0]
        
        table.close()
                    
                    
    def modifyRow(self):
        pass
    
    
    def showClientTable(self):
        
        table = open('clientTable.txt', 'r')
        
        getRows = table.readlines()
        
        table.close()
        
        return getRows