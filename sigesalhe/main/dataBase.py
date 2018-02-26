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
        '''
        Inserts a list of data of a client into the Client table of the data base.
        
        Pre: Takes a list with the validated data of the client.
        
        Pos: It doesn't return anything.
        '''
        table = open('clientTable.txt', 'a')
        
        table.write(lstValidClient[0] + ' NextCamp ' + lstValidClient[1] + ' NextCamp ' + lstValidClient[2] + ' NextCamp ' + lstValidClient[3] + ' NextCamp ' + lstValidClient[4] + ' \n')
        
        table.close()  
        
        
    def findRow(self, query):
        '''
        Seaerches for a match with the query that user passed, and returns the position of the row.
        
        Pre: Takes a string as a query.
        
        Pos: Returns the whole row as a string. 
        '''
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
        '''
        to-do
        '''
        table = open('clientTable.txt', 'w')
        
        pass
        
        table.close()
    
    
    def printRow(self,queryCicles):
        '''
        Prints a row of a table by counting the position of that row in the txt file.
        
        Pre: Takes an integer that determines the number of cicles of the for.
        
        Pos: Returns a string containing the row.
        '''
        table = open('clientTable.txt', 'r')
        for x in range(queryCicles + 1):
            row = table.next()
        return row
        
        table.close()
    
    def showClientTable(self):
        '''
        Prints the whole client table.
        
        Pre: Nothing.
        
        Pos: Returns the whole table as a list.
        '''
        table = open('clientTable.txt', 'r')
        
        getRows = table.readlines()
        
        table.close()
        
        return getRows