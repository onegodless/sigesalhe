#!/usr/bin/python
# -*- coding: latin-1 -*-


'''
Created on Feb 23, 2018

@author: Jesús Molina
'''


class DataBase(object):

    def __init__(self):
        pass
    
    
    def insertClient(self, fileTable, clientData):
        '''
        Inserts a list of strings into a file.
        
        Pre: Takes a list of strings representing the client data.
        
        Pos: Inserts the elements of the list with the format of a table.
        '''
        table = open(fileTable, 'a')
        
        table.write(clientData[0] + ' NextCamp ' + clientData[1] + ' NextCamp ' + clientData[2] + ' NextCamp ' + clientData[3] + ' NextCamp ' + clientData[4] + ' \n')
        
        table.close()  
        
        
    def findRow(self,fileTable,query):
        '''
        Searches for a match with the query that user gives, and returns the position of the row.
        
        Pre: Takes a string as a query.
        
        Pos: Returns the whole row as a string. 
        '''
        table = open(fileTable,'r')
        
        linePos = 0
        allLines = table.readlines()
        for x in allLines:
            splitting = x.split(' NextCamp ')
            for y in splitting:
                if y == query:
                    return linePos
            linePos += 1
                    
        table.close()  
                    
                    
    def modifyRow(self,fileTable,intRow,listFile,modifiedRow):
        '''
        Overwrites a file with the same content as before except for a modified row.
        
        Pre: Takes the position of the row to modify and a list containning the original content of the file.
        
        Pos: Overwrites the file.
        '''
        table = open(fileTable,'w')
        
        listFile[intRow] = modifiedRow
        for x in listFile:
            table.write(x)
            
        table.close()  
    
    
    def printRow(self,fileTable,queryCicles):
        '''
        Prints a row of a table.
        
        Pre: Takes an integer that determines position of the row.
        
        Pos: Returns a string containing the row.
        '''
        table = open(fileTable, 'r')
        for row in range(queryCicles + 1):
            row = table.next()
        return row
        
        table.close()  
    
    def showClientTable(self,fileTable):
        '''
        Prints the whole client table.
        
        Pre: File to open.
        
        Pos: Returns the whole table as a list of strings.
        '''
        table = open(fileTable,'r')
        
        getRows = table.readlines()
        
        table.close()  
        
        return getRows