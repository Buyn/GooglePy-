'''
Created on 27 янв. 2019 г.

@author: BuYn
'''
import unittest
from tkinter import Tk
from view.progressbar import *
from model.tkinterstruct import TKgeovalues
from view.progress3pi import Progres3pi


class Test(unittest.TestCase):


    def setUp(self):
        self.parent = Tk()
        self.tkgeo = TKgeovalues(self.parent)


    def tearDown(self):
        pass


    def testTKinterValueStract(self):
        self.assertIsNotNone(self.tkgeo.parent, "Paren is None")
        self.assertEqual(self.tkgeo.column, 2, "Not Equal")
        self.tkgeo.column = 4
        self.assertEqual(self.tkgeo.column, 4)


    def testProgressBarCreate(self):
        self.progress_bar = ProgressBar(self.tkgeo, 10)
        self.assertIsNotNone(self.progress_bar.bar, "Paren is None")
        self.assertEqual(self.progress_bar.get_value(), 10, "Not Equal")


    def testProgressBarSetValue(self):
        self.progress_bar = ProgressBar(self.tkgeo, 0)
        self.progress_bar.set_value(10)
        self.assertEqual(self.progress_bar.get_value(), 10, "Not Equal")


    def testProgres3piCreate(self):
        self.p3pi = Progres3pi(self.tkgeo, "test")
        self.assertIsNotNone(self.p3pi.pi1)
        self.assertIsNotNone(self.p3pi.pi2)
        self.assertIsNotNone(self.p3pi.pi3)
        self.assertEqual(self.p3pi.pi1.get_value(), 100 )
        self.assertEqual(self.p3pi.pi2.get_value(), 100 )
        self.assertEqual(self.p3pi.pi3.get_value(), 100 )
        self.p3pi.pi1.set_value(80)
        self.assertEqual(self.p3pi.pi1.get_value(), 80 )


    def testLineBarCreate(self):
        from view.todolinecar import ToDolinebar
        self.todoline = ToDolinebar(self.tkgeo, "test")
        self.assertIsNotNone(self.todoline.title_name)
        self.assertIsNotNone(self.todoline.value)
        self.assertIsNotNone(self.todoline.h24)
        self.assertIsNotNone(self.todoline.tuday)
        self.assertIsNotNone(self.todoline.day3)
        self.assertIsNotNone(self.todoline.week)
        self.assertIsNotNone(self.todoline.month)
        self.assertEqual(self.todoline.get_value(), 0)
        self.assertEqual(self.todoline.get_name(), "test")
        self.todoline.set_name("new Test")
        self.assertEqual(
            self.todoline.get_name(), 
            "new Test")
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testProgressBarCreate']
    unittest.main()
