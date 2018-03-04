#!/usr/bin/python
# -*- coding: latin-1 -*-
'''
Created on Feb 25, 2018

@author: Jesús
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
        theFile = self.instDataBase.showClientTable()
        self.instDataBase.modifyRow(5, theFile)
            
            
    def testPrintRow(self): 
        self.assertEqual(self.instDataBase.printRow(3),'45425258Z NextCamp William NextCamp Vasquez NextCamp 545533060 NextCamp 0685 Sanders Point \n')
     
     
    def testFindRow(self):
        self.assertEqual(self.instDataBase.findRow('William'), 3)
        
        
    def testInsertClient(self):
        lstClient = ['12345678A', 'Test', 'Guy', '123456789', 'Fake Street 1', '\n']
        self.instDataBase.insertClient(lstClient)
    
    
    def testShowClientTable(self):  
        print self.instDataBase.showClientTable()
    
            
            
if __name__ == "__main__":
    unittest.main()