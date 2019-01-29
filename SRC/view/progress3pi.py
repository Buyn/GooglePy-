from view.progressbar import ProgressBar
from tkinter import ttk
class Progres3pi(object):
    
    
    def __init__(self, tkgeo, titlename):
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
        self.pi1 = ProgressBar(tkgeo, 100)
        tkgeo.row = 2
        self.pi2 = ProgressBar(tkgeo, 100)
        tkgeo.row = 3
        self.pi3 = ProgressBar(tkgeo, 100)
        tkgeo.row = 4
        text_label = ttk.Label( 
                self.frame, 
                #length=100,
                width = tkgeo.width, 
                text = titlename
                )
        text_label.grid(
                column  = tkgeo.column,
                row     = tkgeo.row,
                sticky  = tkgeo.sticky)



