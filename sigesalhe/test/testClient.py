#! /usr/bin/python
# -*- coding: latin-1 -*-


'''
Created on Feb 23, 2018

@author: Jesús
'''


import unittest
from main.client import Client
from faker import Faker


class Test(unittest.TestCase):


    def setUp(self):
        self.instFaker = Faker()
        self.instClient = Client('45307733X', 'Jesús', 'Molina', '652814940', 'Mar Chica n1 p5 2C')


    def tearDown(self):
        pass


    def testName(self):
        pass
    
    def testValidateValues(self):
        self.assertListEqual(self.instClient.valideteValues(), ['45307733X','Jesús','Molina','652814940','Mar Chica n1 p5 2C'], msg = 'OK')


if __name__ == "__main__":
    unittest.main()