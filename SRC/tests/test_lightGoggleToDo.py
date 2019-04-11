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
        #self.gs.sheet_main.update_acell('A1', 'Bingo!')
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

    def test_compileNewLogString(self):# {{{
        result = self.gs.compileNewLogString(name = "Подготока ОС", time = 12)
        self.assertEqual(
                result
            , ["2/6/2019 6:13:35","","",12,"Подготока ОС","","","","","",
                "=NOW() - A21","=A21-Blans!$O$1",0.07778,"","",
                "=INT(A21)"])
        #   sheet.insertRowBefore(21); 
        #21, 1)("Main")"E4"
        #(21, 3).setValue(value)
        #(21, 4).setValue(time)
        #(21, 5).setValue(name)
        #(21,11).("=NOW() - A21");      
        #(21,12)("=A21-Blans!$O$1");   
        #(21,13)("Calc")("h13")
        #(21,16)("=INT(A21)").setNumberFormat("M/d/yyyy");     
        # }}}
    # }}}
if __name__ == "__main__":# {{{
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    # }}}
