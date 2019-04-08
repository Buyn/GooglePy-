'''
Created on 27 янв. 2019 г.

@author: BuYn
'''
import unittest
from tkinter import Tk
from view.progressbar import *
from model.tkinterstruct import TKgeovalues
from view.progress3pi import Progres3pi
from view.todolinecar import ToDolinebar
from model.globalsvar import *


class Test(unittest.TestCase):


    def setUp(self):
        self.parent = Tk()
        self.tkgeo = TKgeovalues(self.parent)
        self.line = ToDolinebar(self.tkgeo, 'empty0' )


    def tearDown(self):
        pass


    def test_setProgressLine(self):
        vaibls = [1,2,3,4,5]
        self.line.setProgressLine(vaibls)
        self.assertEqual(self.line.lineprogress[0].get_value(), 1)

        
    def test_Init(self):
        self.assertNotEqual(self.line.lineprogress[0], 0)
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testProgressBarCreate']
    unittest.main()
