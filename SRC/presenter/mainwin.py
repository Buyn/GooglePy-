from view.creatwin import initwindow
from view.creatwin import *
from model.globalsvar import *


class mainwindow(object):
    """Initilaze and Creat Main window For App"""

    def reloadfile(self):
        print("button:")


    def __init__(self, title):
        super(mainwindow, self).__init__()
        self.mainwin = initwindow(title)

    
    def mainloop(self):
        self.mainwin.mainloop()

    
    def creatMainWin(self, ):
        #    Win Title
        self.mainwin.text="Reload XML File"
        #    Open Button
        self.mainwin.addne_button( self.reloadfile)
        #    File path field
        self.filepath = StringVar()
        self.mainwin.sticky = (N, W)
        self.mainwin.row = 3
        self.mainwin.column = 2
        self.mainwin.width = 123
        self.filepath.set("button:")
        #self.mainwin.addne_entry( self.filepath)
        # Name Frame with scroll bar list 
        self.mainwin.row = 5
        self.mainwin.column = 2
        self.mainwin.sticky = S
        self.mainwin.width = 120
        self.mainwin.height = 20
        self.valueList = self.mainwin.addne_framelist("Values List ")
        # Name Frame with scroll bar list 
        self.mainwin.row = 6
        self.mainwin.sticky = S
        #self.telemetrilist = self.mainwin.addne_framelist("Pi Chart")
        self.piList = self.mainwin.add_frame()
        self.mainwin.parent = self.piList
        self.mainwin.addne_button( self.reloadfile)
        #self.mainwin.add_pro( self.reloadfile)
        #self.mainwin.parent = self.valueList
        self.mainwin.row = 2
        self.mainwin.column = 1
        self.progressOne = IntVar()
        self.progressOne.set(50)
        self.progressbar = self.mainwin.add_progressbar100( self.progressOne)
        #self.mainwin.parent = self.progressbar
        #self.filepath.set
        self.textPro = self.mainwin.add_text("90%")


