#!/usr/bin/python
# -*- coding: latin-1 -*-


'''
Created on Feb 23, 2018

@author: Jesús
'''


class DataBase(object):

    def __init__(self):
        pass
    
    
    def openTable(self, fileTable, mode):
        '''
        Opens a file a returns it.
        
        Pre: takes the file and the mode we want to open the file wiht.
        
        Post: returns an IO object.
        '''
        fileOpen = open(fileTable, mode)
        return fileOpen
    
    
    def closeTable (self, fileTable):
        '''
        Closes a file.
        '''
        fileTable.close()
        
        
    def insertClient(self,clientData):
        '''
        Inserts a list of data of a client into the Client table of the data base.
        
        Pre: Takes a list of strings representing the client data.
        
        Pos: It doesn't return anything.
        '''
        table = self.openTable('clientTable.txt', 'a')
        
        table.write(clientData[0] + ' NextCamp ' + clientData[1] + ' NextCamp ' + clientData[2] + ' NextCamp ' + clientData[3] + ' NextCamp ' + clientData[4] + ' \n')
        
        self.closeTable(table)  
        
        
    def findRow(self, query):
        '''
        Searches for a match with the query that user passed, and returns the position of the row.
        
        Pre: Takes a string as a query.
        
        Pos: Returns the whole row as a string. 
        '''
        table = self.openTable('clientTable.txt', 'r')
        
        linePos = 0
        allLines = table.readlines()
        for x in allLines:
            splitting = x.split(' NextCamp ')
            for y in splitting:
                if y == query:
                    return linePos
            linePos += 1
                    
        self.closeTable(table)  
                    
                    
    def modifyRow(self, row, fileTable):
        '''
        to-do
        '''
        table = self.openTable('clientTable.txt', 'w')
        
        fileTable[row] = '45307733X NextCamp Antonio NextCamp Campillos NextCamp 652871494 NextCamp Mar Chica n1 p5 2C \n'
        for x in fileTable:
            table.write(x)
            
        self.closeTable(table)  
    
    
    def printRow(self,queryCicles):
        '''
        Prints a row of a table by counting the position of that row in the txt file.
        
        Pre: Takes an integer that determines the number of cicles of the for.
        
        Pos: Returns a string containing the row.
        '''
        table = self.openTable('clientTable.txt', 'r')
        for x in range(queryCicles + 1):
            row = table.next()
        return row
        
        self.closeTable(table)  
    
    def showClientTable(self):
        '''
        Prints the whole client table.
        
        Pre: Nothing.
        
        Pos: Returns the whole table as a list.
        '''
        table = self.openTable('clientTable.txt', 'r')
        
        getRows = table.readlines()
        
        self.closeTable(table)  
        
        return getRows