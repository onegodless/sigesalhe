#! /usr/bin/python
# -*- coding: latin-1 -*-


'''
Created on Feb 23, 2018

@author: Jesús Molina
'''


import unittest
from main.client import Client


class Test(unittest.TestCase):


    def setUp(self):
        self.instClient = Client('45307733X', 'Jesús', 'Molina', '652814940', 'Mar Chica n1 p5 2C')


    def tearDown(self):
        pass


    def testName(self):
        pass
    
    def testSTR(self):
        print self.instClient
    
    def testValidateValues(self):
        self.assertListEqual(self.instClient.validateValues(), ['45307733X','Jesús','Molina','652814940','Mar Chica n1 p5 2C'])


if __name__ == "__main__":
    unittest.main()