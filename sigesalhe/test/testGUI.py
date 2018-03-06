#!/usr/bin/python
# -*- coding: latin-1 -*-

'''
Created on Feb 24, 2018

@author: Jesús Molina
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
        print self.instGUI.printMenu(self.instGUI.getMainMenu())
        self.instGUI.clearScreen()
    
    def testcaptureInput(self):
        selection = self.instGUI.captureInput(self.instGUI.getMainMenu())
        self.assertEqual(selection,1)

if __name__ == "__main__":
    unittest.main()