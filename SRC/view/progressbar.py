from tkinter import StringVar, IntVar
from tkinter import ttk
from model.tkinterstruct import TKgeovalues
import copy


class ProgressBar(object):
    
    
    def __init__(self, newtkvalues, startvalue):
        tkvalues = copy.copy(newtkvalues)
        self.value = IntVar() 
        self.value.set(startvalue)
        self.bar = ttk.Progressbar( 
                tkvalues.parent,
                orient  = tkvalues.orient,
                mode    = tkvalues.mode,
                length  = tkvalues.length,
                variable = self.value
                )
        self.bar.grid(
                column  = tkvalues.column,
                row     = tkvalues.row,
                sticky  = tkvalues.sticky)

    
    def get_value(self):
        return self.value.get()

    
    def set_value(self, newvalue):
        self.value.set(newvalue)
    
    
    
    
    
    



