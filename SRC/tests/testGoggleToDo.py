'''
Created on 28 янв. 2019 г.

@author: BuYn
'''
import unittest
from model.globalsvar import *
from presenter.gstodo import GSTodo

class Test(unittest.TestCase):


    @classmethod
    def setUpClass(self):
        print("*"*33,"*"*33)
        self.gs = GSTodo()
        # use creds to create a client to interact with the Google Drive API
        print ("file opened")
        print("*"*33,"*"*33)
        self.gs.sheet_main.update_acell('A1', 'Bingo!')

        
    @classmethod
    def tearDownClass(cls):
        print("*"*33,"*"*33)
        print("tear down module")
        print("*"*33,"*"*33)


    def setUp(self):
        i ="set up"
        print("*"*33,i,"*"*33)



    def tearDown(self):
        i = "tear Down"
        print("*"*33,i,"*"*33)


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


    def testGetNameList(self):
        sheet = self.gs.sheet_main
        print(self.gs.getNameList()) 
        self.assertEqual(
            self.gs.getNameList()[0].value, 
            self.gs.file.worksheet(TD_MAINSHEET).acell('G3').value)
        
        
    def testGetListOfprogressForCell(self):
        sheet = self.gs.sheet_main
        print(self.gs.getListOfProgressForCell(self.gs.sheet_main.acell('G3'))) 
        self.assertEqual(
            self.gs.getListOfProgressForCell(self.gs.sheet_main.acell('G3'))[0], 
            self.gs.file.worksheet(TD_MAINSHEET).acell('F3').value)
        
        
    def testGetPiListOfprogressBarForCell(self):
        sheet = self.gs.sheet_calc
        print(self.gs.getPiListOfProgressBarForCell(
            sheet.acell(TD_PI24H))) 
        self.assertEqual(
            self.gs.getPiListOfProgressBarForCell(
                sheet.acell(TD_PI24H))[0], 
            sheet.acell(TD_PI24H).value)
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()