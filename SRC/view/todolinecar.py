from tkinter import ttk, StringVar, IntVar
from view.progressbar import ProgressBar
import copy
from model.globalsvar import *
class ToDolinebar(object):
    def __init__(self, tmp_tkgeo, starttext):
        tkgeo = copy.copy(tmp_tkgeo)
        self.frame  = ttk.Frame(tkgeo.parent, padding="1 1 1 1")
        self.frame.grid(
                column  = tkgeo.column,
                row     = tkgeo.row,
                sticky  = tkgeo.sticky)
        
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        tkgeo.parent = self.frame
        tkgeo.column = 1
        tkgeo.row = 1
        self.value = IntVar()
        self.value.set(0)
        tkgeo.width = 20  
        self.title_name  = StringVar()
        self.title_name.set(starttext)
        text_label = ttk.Label( 
                self.frame , 
                width = tkgeo.width 
#                 ,text = self.title_name.get()
                ,textvariable = self.title_name
                )
        text_label.grid(
                column  = tkgeo.column,
                row     = tkgeo.row,
                sticky  = tkgeo.sticky)
#         self.title_name.set(starttext)
        tkgeo.row = 1
        tkgeo.column = 2
        tkgeo.width = 5  
        entry = ttk.Entry( 
                tkgeo.parent, 
                width = tkgeo.width, 
                textvariable = self.value
                )
        entry.grid(
                column  = tkgeo.column,
                row     = tkgeo.row,
                sticky  = tkgeo.sticky)
        tkgeo.row = 1
        tkgeo.column = 4
        tkgeo.length = 50
        self.lineprogress = [1,2,3,4,5,6]
        for j in WI_TODOPROGRESBAR.items():
            tkgeo.column = 5 +j[1]
            self.lineprogress[j[1]] = ProgressBar(tkgeo, 0)

    
    def get_value(self):
        return self.value.get()

    
    def get_name(self):
        return self.title_name.get()
    
    
    def set_name(self, newtext):
        return self.title_name.set(newtext)

    
    def setProgressLine(self, variblist):
        for i in range(len(WI_TODOPROGRESBAR)):
            self.lineprogress[i].set_value(variblist[i])
    
