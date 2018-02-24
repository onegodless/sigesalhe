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
        
        
    def findRow(self, query):
        
        table = open('clientTable.txt', 'r')
        
        linePos = 0
        allLines = table.readlines()
        for x in allLines:
            splitting = x.split(' NextCamp ')
            for y in splitting:
                if y == query:
                    return linePos
            linePos += 1
                    
        table.close()
                    
                    
    def modifyRow(self, row):
        table = open('clientTable.txt', 'w')
        
        table.close()
    
    
    def printRow(self,queryPos):
        
        table = open('clientTable.txt', 'r')
        for x in range(queryPos + 1):
            actualPos = table.next()
        print actualPos
        
        table.close()
    
    def showClientTable(self):
        
        table = open('clientTable.txt', 'r')
        
        getRows = table.readlines()
        
        table.close()
        
        return getRows