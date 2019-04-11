'''# {{{
Created on 27 янв. 2019 г.

@author: BuYn
'''# }}}
import unittest# {{{
from tkinter import Tk
from view.progressbar import *
from model.tkinterstruct import TKgeovalues
from view.progress3pi import Progres3pi
from view.todolinecar import ToDolinebar
from model.globalsvar import *
# }}}

class Test(unittest.TestCase):# {{{

    def setUp(self):# {{{
        self.parent = Tk()
        self.tkgeo = TKgeovalues(self.parent)
# }}}

    def tearDown(self):# {{{
        pass
# }}}

    def testTKinterValueStract(self):# {{{
        self.assertIsNotNone(self.tkgeo.parent, "Paren is None")
        self.assertEqual(self.tkgeo.column, 2, "Not Equal")
        self.tkgeo.column = 4
        self.assertEqual(self.tkgeo.column, 4)
# }}}

    def testProgressBarCreate(self):# {{{
        self.progress_bar = ProgressBar(self.tkgeo, 10)
        self.assertIsNotNone(self.progress_bar.bar, "Paren is None")
        self.assertEqual(self.progress_bar.get_value(), 10, "Not Equal")
# }}}

    def testProgressBarSetValue(self):# {{{
        self.progress_bar = ProgressBar(self.tkgeo, 0)
        self.progress_bar.set_value(10)
        self.assertEqual(self.progress_bar.get_value(), 10, "Not Equal")
# }}}

    def testProgres3piCreate(self):# {{{
        self.p3pi = Progres3pi(self.tkgeo, "test")
        self.assertIsNotNone(self.p3pi.pi1)
        self.assertIsNotNone(self.p3pi.pi2)
        self.assertIsNotNone(self.p3pi.pi3)
        self.assertEqual(self.p3pi.pi1.get_value(), 100 )
        self.assertEqual(self.p3pi.pi2.get_value(), 100 )
        self.assertEqual(self.p3pi.pi3.get_value(), 100 )
        self.p3pi.pi1.set_value(80)
        self.assertEqual(self.p3pi.pi1.get_value(), 80 )
# }}}

    def testLineBarCreate(self):# {{{
        self.todoline = ToDolinebar(self.tkgeo, "test")
        self.assertIsNotNone(self.todoline.title_name)
        self.assertIsNotNone(self.todoline.value)
        for i in range(len(WI_TODOPROGRESBAR)):
            self.assertIsNotNone(self.todoline.lineprogress[i])
        self.assertEqual(self.todoline.get_value(), 0)
        self.assertEqual(self.todoline.get_name(), "test")
        self.todoline.set_name("new Test")
        self.assertEqual(
            self.todoline.get_name(), 
            "new Test")
        self.assertEqual(
            self.tkgeo.parent, 
            self.parent,
            "Parent is lost")
        self.todoline1 = ToDolinebar(self.tkgeo, "test1")
        print(self.todoline1.get_name())
        self.assertEqual(
            self.todoline1.get_name(), 
            "test1",
            "text1 is lost")
        print(self.todoline.get_name())
        self.assertEqual(
            self.todoline.get_name(), 
            "new Test",
            "text is lost")
        todo = [1,2,3,4,5]
        for j in WI_TODOPROGRESBAR.items():
            print(j, j[0], j[1])
            todo[j[1]] = ToDolinebar(self.tkgeo, j[0])
        for j in WI_TODOPROGRESBAR.keys():
            print(j, WI_TODOPROGRESBAR.get(j) )
            print(todo[WI_TODOPROGRESBAR.get(j)])
            self.assertIsNotNone(todo[WI_TODOPROGRESBAR.get(j)])
            # }}}

    def test_LineBarSetValue(self):# {{{
        self.todoline = ToDolinebar(self.tkgeo, "test")
        for i in range(len(WI_TODOPROGRESBAR)):
            self.assertIsNotNone(self.todoline.lineprogress[i])
        self.todoline1 = ToDolinebar(self.tkgeo, "test1")
        self.todoline1.setProgressLine([10,20,30,40,50])
        self.assertEqual(self.todoline1.lineprogress[0].value.get(), 10)
        print(self.todoline1.lineprogress[0].value.get())
        self.assertEqual(self.todoline1.lineprogress[4].value.get(), 50)
            # }}}

    # }}}
if __name__ == "__main__":# {{{
    #import sys;sys.argv = ['', 'Test.testProgressBarCreate']
    unittest.main()
# }}}
