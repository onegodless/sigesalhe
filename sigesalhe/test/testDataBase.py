#!/usr/bin/python
# -*- coding: latin-1 -*-
'''
Created on Feb 25, 2018

@author: Jesús Molina
'''
import unittest
from main.dataBase import DataBase
from faker import Faker

class Test(unittest.TestCase):


    
            
    def setUp(self):
        self.instDataBase = DataBase()
        self.fakerMachine = Faker()
    
    
    def tearDown(self):
        pass
 
 
    def testName(self):
        pass
 
 
    def testModifyRow(self):
        listFile = self.instDataBase.showClientTable('clientTable.txt')
        modifiedRow = '45325756A NextCamp Test NextCamp Joe NextCamp 541533660 NextCamp Faky street 1 \n'
        self.instDataBase.modifyRow('clientTable.txt',5,listFile, modifiedRow)
            
            
    def testPrintRow(self): 
        self.assertEqual(self.instDataBase.printRow('clientTable.txt',3),'45425258Z NextCamp William NextCamp Vasquez NextCamp 545533060 NextCamp 0685 Sanders Point \n')
     
     
    def testFindRow(self):
        self.assertEqual(self.instDataBase.findRow('clientTable.txt','William'),3)
        
        
    def testInsertClient(self):
        lstClient = ['12345678A', 'Test', 'Guy', '123456789', 'Fake Street 1', '\n']
        self.instDataBase.insertClient('clientTable.txt',lstClient)
    
    
    def testShowClientTable(self):  
        listTable = self.instDataBase.showClientTable('clientTable.txt')
        for x in listTable:
            print x
            
            
if __name__ == "__main__":
    unittest.main()