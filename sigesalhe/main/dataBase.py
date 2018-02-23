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
        
        table = open('clientTable.txt', 'a+')
        
        table.write(lstValidClient[0] + 'NextCamp' + lstValidClient[1] + 'NextCamp' + lstValidClient[2] + 'NextCamp' + lstValidClient[3] + 'NextCamp' + lstValidClient[4] + ' \n')
        
        table.seek(0)
        firstLine = table.readline()
        firstLineSplit = firstLine.split('NextCamp')
        print firstLineSplit
        
        table.close()        