#!/usr/bin/python
# -*- coding: latin-1 -*-

'''
Created on Feb 24, 2018

@author: Jesús
'''
import unittest
from main.gui import GUI

class Test(unittest.TestCase):


    def setUp(self):
        self.instGUI = GUI()


    def tearDown(self):
        pass


    def testName(self):
        pass
    
    def testPrintMenu(self):
        print self.instGUI.printMenu(self.instGUI.mainMenu)
        self.instGUI.clearScreen()
    
    def testcaptureInput(self):
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()