'''# {{{
Created on 28 янв. 2019 г.

@author: BuYn
'''# }}}
#import block# {{{
import unittest
from model.globalsvar import *
from presenter.gstodo import GSTodo
# }}}
class Test(unittest.TestCase):# {{{

    @classmethod #setUpClass# {{{
    def setUpClass(self):
        print("*"*33,"*"*33)
        self.gs = GSTodo(filename = 'testToDoProgresDaylis')
#        https://docs.google.com/spreadsheets/d/15EjV7CfotRunq831Ca1yWXtsI04DcVS_ukX0fHs6O7k/edit#gid=0
        # use creds to create a client to interact with the Google Drive API
        print ("file opened")
        print("*"*33,"*"*33)
        self.gs.sheet_main.update_acell('A1', 'Bingo!')
        # }}}
        
    @classmethod #tearDownClass# {{{
    def tearDownClass(cls):
        print("*"*33,"*"*33)
        print("tear down module")
        print("*"*33,"*"*33)
# }}}

    def setUp(self):# {{{
        i ="set up"
        print("*"*33,i,"*"*33)
# }}}

    def tearDown(self):# {{{
        i = "tear Down"
        print("*"*33,i,"*"*33)
# }}}

    def test_init(self):# {{{
        self.assertIsNotNone( self.gs.sheet_main)
        self.assertIsNotNone( self.gs.sheet_main.sheet)
        self.assertIsNotNone( self.gs.sheet_calc.sheet)
        print(self.gs.sheet_main.sheet)
        # }}}

    def test_atoarint(self):# {{{
        self.assertEqual(
            self.gs.sheet_main.atoarrint("E3")
            , [5,3])
        self.assertEqual(
            self.gs.sheet_main.atoarrint("E2")
            , [5,2])
        self.assertEqual(
            self.gs.sheet_main.atoarrint("A2")
            , [1,2])
        self.assertEqual(
            self.gs.sheet_main.atoarrint("A12")
            , [1,12])
        # }}}

    def test_atoint(self):# {{{
        self.assertEqual(
            self.gs.sheet_main.atoint("E")
            , 5)
        self.assertEqual(
            self.gs.sheet_main.atoint("c")
            , 3)
        self.assertEqual(
            self.gs.sheet_main.atoint("A")
            , 1)
        # }}}

    def testGetTimeStump(self):# {{{
        sheet = self.gs.sheet_main
        # Extract and print the values
        print( self.gs.getTimeStump())
        print( self.gs.getTimeStump("E3"))
        # exempl =  1/29/2019 12:00:10 
        self.assertEqual(
            self.gs.getTimeStump( "E3")
            , '00:01:00')
        # }}}

    def testGetprogressTo100sum(self):# {{{
        sheet = self.gs.sheet_calc
        print(self.gs.getProgressTo100Sum()) 
        print(self.gs.sheet_calc.acell("a10").value) 
        print(self.gs.sheet_calc.acell("a11").value) 
        print(self.gs.sheet_calc.acell("a12").value) 
        print(self.gs.sheet_calc.acell("a13").value) 
        print(self.gs.sheet_calc.acell("a14").value) 
        print(self.gs.sheet_calc.acell("a15").value) 
        self.assertEqual(
            self.gs.getProgressTo100Sum() , 
            self.gs.file.worksheet(
                TD_CALCSHEET).acell(
                    TD_SUMPROGRESS100).value)
# }}}

    def testGetNameList(self):# {{{
        sheet = self.gs.sheet_main
        print(self.gs.getNameList()) 
        print(self.gs.getNameList()[0].value)
        self.assertEqual(
            self.gs.getNameList()[0].value, 
            self.gs.file.worksheet(TD_MAINSHEET).acell('G3').value)
        # }}}
        
    def testGetListOfprogressForCell(self):# {{{
        sheet = self.gs.sheet_main
        print(self.gs.getListOfProgressForCell(self.gs.sheet_main.acell('G3'))) 
        self.assertEqual(
            self.gs.getListOfProgressForCell(self.gs.sheet_main.acell('G3'))[0], 
            self.gs.file.worksheet(TD_MAINSHEET).acell('F3').value)
        # }}}
        
    def test_getCellFromMain(self):# {{{
        name = 'G3'
        i =1
        name = "G" + str(3 +i)
        print(name)
        self.assertEqual(self.gs.getCellFromMain(name).value,
                         self.gs.sheet_main.acell(name).value)
        # }}}
        
    def testGetPiListOfprogressBarForCell(self):# {{{
        sheet = self.gs.sheet_calc
        print(self.gs.getPiListOfProgressBarForCell(
            TD_PI24H)) 
        self.assertEqual(
            self.gs.getPiListOfProgressBarForCell(
                TD_PI24H)[0], 0)
        self.assertEqual(
            self.gs.getPiListOfProgressBarForCell(
                TD_PI24H)[2], 114)
        # }}}
        # }}}
if __name__ == "__main__":# {{{
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    # }}}
