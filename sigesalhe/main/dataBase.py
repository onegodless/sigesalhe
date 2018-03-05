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
        __table = open(fileTable, 'a')
        
        __table.write(clientData[0] + ' NextCamp ' + clientData[1] + ' NextCamp ' + clientData[2] + ' NextCamp ' + clientData[3] + ' NextCamp ' + clientData[4] + ' \n')
        
        __table.close()  
        
        
    def findRow(self,fileTable,query):
        '''
        Searches for a match with the query that user gives, and returns the position of the row.
        
        Pre: Takes a string as a query.
        
        Pos: Returns the whole row as a string. 
        '''
        __table = open(fileTable,'r')
        
        __linePos = 0
        __allLines = __table.readlines()
        for x in __allLines:
            __splitting = x.split(' NextCamp ')
            for y in __splitting:
                if y == query:
                    return __linePos
            __linePos += 1
                    
        __table.close()  
                    
                    
    def modifyRow(self,fileTable,intRow,listFile,modifiedRow):
        '''
        Overwrites a file with the same content as before except for a modified row.
        
        Pre: Takes the position of the row to modify and a list containning the original content of the file.
        
        Pos: Overwrites the file.
        '''
        __table = open(fileTable,'w')
        
        listFile[intRow] = modifiedRow
        for __x in listFile:
            __table.write(__x)
            
        __table.close()  
    
    
    def printRow(self,fileTable,queryCicles):
        '''
        Prints a row of a table.
        
        Pre: Takes an integer that determines position of the row.
        
        Pos: Returns a string containing the row.
        '''
        __table = open(fileTable, 'r')
        for __row in range(queryCicles + 1):
            __row = __table.next()
        return __row
        
        __table.close()  
    
    def showClientTable(self,fileTable):
        '''
        Prints the whole client table.
        
        Pre: File to open.
        
        Pos: Returns the whole table as a list of strings.
        '''
        __table = open(fileTable,'r')
        
        __getRows = __table.readlines()
        
        __table.close()  
        
        return __getRows