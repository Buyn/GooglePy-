'''
Created on 28 янв. 2019 г.

@author: BuYn
'''
import unittest
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from model.globalsvar import *
from presenter.gstodo import GSTodo

class Test(unittest.TestCase):


    @classmethod
    def setUpClass(self):
        self.gs = GSTodo()
        # use creds to create a client to interact with the Google Drive API
        print ("file opened")
        self.gs.sheet_main.update_acell('A1', 'Bingo!')

        
    @classmethod
    def tearDownClass(cls):
        print("tear down modeule")


    def setUp(self):
        print("set up")


    def tearDown(self):
        pass


    def testGetTimeStump(self):
        sheet = self.gs.sheet_main
        # Extract and print the values
        print( self.gs.getTimeStump())
        print( self.gs.getTimeStump("E3"))
        # exempl =  1/29/2019 12:00:10 
        self.assertEqual(
            self.gs.getTimeStump( "E3")
            , '00:01:00')


    def testGetprogressTo100sum(self):
        sheet = self.gs.sheet_calc
        print(self.gs.getProgressTo100Sum()) 
        self.assertEqual(
            self.gs.getProgressTo100Sum() , 
            self.gs.file.worksheet(TD_CALCSHEET).acell(TD_SUMPROGRESS100).value)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()